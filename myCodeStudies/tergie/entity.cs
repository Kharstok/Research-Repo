namespace Tergie.source
{
    public class Entity
    {
        public Vector2I Pos { get; set; }
        public int Width { get; set; }
        public int Height { get; set; }
        public char[,] Characters { get; set; }

        public Entity(char[,] characters)
        {
            Pos = new Vestor2I(x:0,y:0);
            Characters = characters;
            Width = Characters.GetLength(dimension:1;);
            Height = Characters.GetLength(dimension:0);
        }
    }
}