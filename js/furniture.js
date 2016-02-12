

var FURNITURE_DATA = 
[
    ["bed", "media/bed.obj", 0xffffff],
    ["couch", "media/bed.obj", 0xffffff],
    ["desk", "media/bed.obj", 0xffffff],
    ["chair", "media/bed.obj", 0xffffff],
    ["tv", "media/bed.obj", 0xffffff],
    ["tabe", "media/bed.obj", 0xffffff],
    ["carpet", "media/bed.obj", 0xffffff],
    ["shelf", "media/bed.obj", 0xffffff],
];

var furnitureModels = [];

function loadFurnitureModel(name, pos, angle)
{

    modelData = getModelData(name);

    objLoader.load( "media/bed.obj", function ( object ) {
        object.traverse( function ( child ) {

            if ( child instanceof THREE.Mesh ) {

                //child.material.map = texture;
                child.material = defaultMaterial.clone();
                child.material.color = modelData[2];
            }

        } );

        //object.scale.set(0.3, 0.3, 0.3);

        object.position.copy(pos);
        object.rotation.y = angle;

        furnitureModels.push({name: name, object:object});

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

