

var FURNITURE_DATA = 
[
    ["bed", "media/bed.obj", 0xff8888, [0.9, 0.75, 2.0]],
    ["couch", "media/couch.obj", 0x835339, [0.8, 0.8, 2.5]],
    ["desk", "media/desk.obj", 0xffffff, [0.7, 1, 1.5]],
    ["chair", "media/chair.obj", 0x8888ff, [0.6, 0.6, 0.6]],
    ["tv", "media/bed.obj", 0xffffff],
    ["table", "media/table.obj", 0xffffff],
    ["carpet", "media/bed.obj", 0xffffff],
    ["shelf", "media/bed.obj", 0xffffff],
    ["door", "media/door.obj", 0xffffff, [0.9, 1, 1]],
    ["window", "media/window.obj", 0xffffff, [0.9, 1, 1]],
];

function loadFurnitureModel(name, pos, angle)
{
    var modelData = getModelData(name);

    objLoader.load( modelData[1], function ( object ) {
        object.traverse( function ( child ) {

            if ( child instanceof THREE.Mesh ) {

                //child.material.map = texture;
                //child.material = defaultMaterial;
                child.material = new THREE.MeshPhongMaterial({
                            specular: 0x111111,
                            shininess: 0,
                            color: modelData[2]
                        });
            }

        } );

        //object.scale.set(0.3, 0.3, 0.3);

        object.position.copy(pos);
        object.rotation.y = angle;
        object.scale.set(modelData[3][0], modelData[3][1], modelData[3][2]);

        scene.add(object);
    }, function(){}, function(){} );
}

function getModelData(name)
{
    for(var i = 0; i < FURNITURE_DATA.length; i++)
    {
        if(FURNITURE_DATA[i][0] == name)
        {
            return FURNITURE_DATA[i];
        }
    }

    console.log("No furniture " + name);
}

