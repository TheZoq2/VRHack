
var objLoader = new THREE.OBJLoader( manager );

var modelData
[
    ["bed", "media/bed.obj"],
    ["couch", "media/bed.obj"],
    ["desk", "media/bed.obj"],
    ["chair", "media/bed.obj"],
    ["tv", "media/bed.obj"],
    ["tabe", "media/bed.obj"],
    ["carpet", "media/bed.obj"],
    ["shelf", "media/bed.obj"],
];

function loadFurnitureModel(name, pos, angle)
{
    loader.load( getFurniturePath(name), function ( object ) {
        object.traverse( function ( child ) {

            if ( child instanceof THREE.Mesh ) {

                //child.material.map = texture;
                child.material = new THREE.MeshPhongMaterial( { 
                        color: 0x333333, 
                        specular: 0x333333, 
                        shininess: 50
                    })

            }

        } );

        object.scale.set(0.3, 0.3, 0.3);

        object.position.copy(pos);
        object.rotation.y = angle;

        furnitureModels.push({name: name, object:object});
    }, function(){}, function(){} );
}

function getFurniturePath(name)
{
    for(var i = 0; i < furnitureModels.length; i++)
    {
        if(modelData[i][0] == name)
        {
            return modelData[i][1];
        }
    }

    console.log("No furniture " + name);
}

