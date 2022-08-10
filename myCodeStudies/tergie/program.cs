namespace Tergie.source
{
    class Program
    {
        static void Main(string[] args)
        {
            // create a Scene
            Scene scene = new Scene(width:100,height:100)

            // add Entitites to Scene
            Entity e = new Entity(characters:Utils.FileToCharArray("../../../resources/a"))
            scene.AddEntity(e);
            e.Pos = new Vestor2I(x:0,y:0);

            // start game
            Game.Start(scene);
        }
    }
}

