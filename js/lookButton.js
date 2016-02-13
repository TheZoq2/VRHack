var lookButtons = [];

var lookButtonMaterial;

var defaultScale = 0.2;
var expandedScale = 0.2;

function LookButton(pos, onTrigger)
{
    this.pos = pos;
    this.sprite = new THREE.Sprite(lookButtonMaterial);

    this.sprite.position = pos;
    this.sprite.scale.set(0.2, 0.2, 0.2);
    scene.add(this.sprite);

    this.startLook = 0;
    this.isLooked = false;

    this.doButton = function(camera)
    {
        //Calculate distance to button
        var diff = this.pos.clone().sub(camera.position);

        var viewDir = camera.getWorldDirection();

        var angleDiff = diff.angleTo(viewDir);

        if(Math.abs(angleDiff) < Math.PI / 15)
        {
            if(this.isLooked == false)
            {
                this.startLook = Date.now();
                this.isLooked = true;
            }

            //var newScale = defaultScale + expandedScale * 
            this.sprite.scale.se
        }
        else
        {
            this.isLooked = false;
        }
    }

    this.setPosition = function(pos)
    {
        this.pos = pos;
        this.sprite.position.copy(pos);
    }

    this.onTrigger = onTrigger;
}

function loadLookButtonMedia()
{
    var tLoader = new THREE.TextureLoader();
    var texture = tLoader.load("media/lookButton.png");
    
    lookButtonMaterial = new  THREE.SpriteMaterial({map: texture, color: 0xffffff});
}

function addLookButton(pos, onTrigger)
{
    lookButtons.push(new LookButton(pos, onTrigger));

    console.log(lookButtons.length);
    return lookButtons[lookButtons.length - 1];
}

function updateLookButtons(camera)
{
    for(var i = 0; i < lookButtons.length; i++)
    {
        lookButtons[i].doButton(camera);
    }
}
