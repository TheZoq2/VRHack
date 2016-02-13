var roomSize = 5;
var roofHeight = 2.3;
var headHeight = 1.5;

var WALL_COLOR = 0xffffff;
var LAMP_COLOR = 0xfcffd4;

var roomCube;

var defaultMaterial;
var objLoader;
var scene;

function main()
{
    // Setup three.js WebGL renderer. Note: Antialiasing is a big performance hit.
    // Only enable it if you actually need to.
    var renderer = new THREE.WebGLRenderer({antialias: true});
    renderer.setPixelRatio(window.devicePixelRatio);

    // Append the canvas element created by the renderer to document body element.
    document.body.appendChild(renderer.domElement);

    // Create a three.js scene.
    scene = new THREE.Scene();

    // Create a three.js camera.
    var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 10000);

    // Apply VR headset positional data to camera.
    var controls = new THREE.VRControls(camera);

    // Apply VR stereo rendering to renderer.
    var effect = new THREE.VREffect(renderer);
    effect.setSize(window.innerWidth, window.innerHeight);


    defaultMaterial = new THREE.MeshPhongMaterial({
                            specular: 0x111111,
                            shininess: 5,
                        });

    objLoader = new THREE.OBJLoader( manager );
    // Add a repeating grid as a skybox.
    //var boxWidth = 5;
    //var loader = new THREE.TextureLoader();
    //loader.load('img/box.png', onTextureLoaded);

    //function onTextureLoaded(texture) {
    //    texture.wrapS = THREE.RepeatWrapping;
    //    texture.wrapT = THREE.RepeatWrapping;
    //    texture.repeat.set(boxWidth, boxWidth);

    //    var geometry = new THREE.BoxGeometry(boxWidth, boxWidth, boxWidth);
    //    var material = new THREE.MeshBasicMaterial({
    //        map: texture,
    //        color: 0x01BE00,
    //        side: THREE.BackSide
    //    });

    //    var skybox = new THREE.Mesh(geometry, material);
    //    scene.add(skybox);
    //}


    
    var lampGeometry = new THREE.SphereGeometry(1,32,32);
    var lampMaterial = new THREE.MeshPhongMaterial({
                color: LAMP_COLOR,
                emissive: LAMP_COLOR
            });
    var lamp = new THREE.Mesh(lampGeometry, lampMaterial);
    lamp.scale.set(0.2, 0.1, 0.2);
    lamp.position.y = roofHeight;
    scene.add(lamp);

    
    var lamp = new THREE.Mesh(
            );
    var light = new THREE.PointLight(LAMP_COLOR, 1, 6);
    light.position.y = roofHeight - 0.2;
    scene.add(light);

    var ambiLight = new THREE.AmbientLight(0x404040);
    scene.add(ambiLight);
    
    roomCube = new THREE.Mesh(
                new THREE.BoxGeometry(roomSize, roofHeight, roomSize),
                new THREE.MeshPhongMaterial({
                    color: WALL_COLOR,
                    specular: 0x111111,
                    shininess: 5,
                    side: THREE.BackSide
                }));
    roomCube.position.set(0,roofHeight / 2, 0);

    scene.add(roomCube);

    // Create a VR manager helper to enter and exit VR mode.
    var params = {
        hideButton: false, // Default: false.
        isUndistorted: false // Default: false.
    };
    var manager = new WebVRManager(renderer, effect, params);

    // Create 3D objects.
    var geometry = new THREE.BoxGeometry(0.5, 0.5, 0.5);
    var material = new THREE.MeshNormalMaterial();
    var cube = new THREE.Mesh(geometry, material);

    // Position cube mesh
    cube.position.z = -1;
    cube.position.y = 0.25;

    // Add cube mesh to your three.js scene
    //scene.add(cube);

    //Setup viewpoints
    loadLookButtonMedia();
    var toggleMoveButton = addLookButton(new THREE.Vector3(0,0,0), function(){console.log("movement toggled")});

    //Creating the actual furniture
    for(var i = 0; i < furnitures.length; i++)
    {
        f = furnitures[i];

        var pos = new THREE.Vector3(f[1] / 100, 0, f[2]/ 100);
        pos.sub(new THREE.Vector3(2.5, 0, 2.5));
        loadFurnitureModel(f[0], pos, f[3] * Math.PI / 180);
    }
    

    camera.position.set(2, headHeight, 2);

    // Request animation frame loop function
    var lastRender = 0;
    function animate(timestamp) {
        var delta = Math.min(timestamp - lastRender, 500);
        lastRender = timestamp;

        var toggleMovePos = camera.position.clone();
        toggleMovePos.y += 0.3;
        //toggleMovePos.set(0,1,0);
        toggleMoveButton.setPosition(toggleMovePos);

        updateLookButtons(camera);

        // Apply rotation to cube mesh
        cube.rotation.y += delta * 0.0006;

        // Update VR headset position and apply to camera.
        controls.update();

        // Render the scene through the manager.
        manager.render(scene, camera, timestamp);

        requestAnimationFrame(animate);
    }

    // Kick off animation loop
    animate(performance ? performance.now() : Date.now());

    // Reset the position sensor when 'z' pressed.
    function onKey(event) {
      if (event.keyCode == 90) { // z
        controls.resetSensor();
      }
    }

    window.addEventListener('keydown', onKey, true);
}
