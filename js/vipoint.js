var viewpoints = [];

function Viewpoint(pos)
{
    this.isCurrent = false;
    this.pos = pos;
}

function addViewpoint(pos)
{
    viewpoints.push(new Viewpoint(pos));
}
