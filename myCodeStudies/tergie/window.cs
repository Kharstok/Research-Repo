       // below starts at line 4
    {
        public class Window
        {
            private Vector2I _pos = new Vector2I(x:0,y:0);

            public Scene Scene { get; set; }
            public int Width => Console.WindowWidth;
            public int Height => Console.WindowHeight;

            public Window(Scene scene)
            {
                Scene = scene;
            }

            public Vector2I Pos
            {
                get => _pos;
                set
                {
                    _pos= value;
                }
            }

            /// <summary>
            /// Convert a position in window space to scene space
            /// </summary>
            public Vector2I WindowToScene(Vector2I windowPos)
            {
                return new Vector2I(x:_pos.X + windowPos.X,y:_pos.Y + windowPos.Y);
            }

            /// <summary>
            /// Convert a postion in scene space to window space
            /// </summary>
            public Vector2I SceneToWindow(Vector2I scenePos)
            {
                return new Vector2I(x:scenePos.X - _pos.X,y:scenePos.Y - _pos.Y);
            }
    
        /// <summary>
        /// Draw the region of the scene that is visible through the window.
        /// </summary>

        public void Draw()
        {
            Console.SetCursorPosition(left:0,top:0);
            for (int i = 0; i < Height; i++)
            {
                for(int j = 0; j < Width; j++)
                {
                    Vestor2I scenePos = WindowToScene(windowpos: new Vector2I(x:j, y:i))
                    if (Scene.IsInBounds(scenePos))
                    {
                        char c = (Scene.ChartAt(scenePos));
                        Console.Write(c);
                    }
                    else
                    {
                        Console.Write(' ');
                    }
                }
            }
        }

        public void Update(float dtMilliseconds)
        {
            if(Game.PressedKeys.Contains(item:ConsoleKey.W))
            _pos.Y -= 1;
            if(Game.PressedKeys.Contains(item:ConsoleKey.S))
            _pos.Y += 1;
            if(Game.PressedKeys.Contains(item:ConsoleKey.A))
            _pos.X -= 1;
            if(Game.PressedKeys.Contains(item:ConsoleKey.D))
            _pos.X += 1;

            Scene.Update(dtMilliseconds);
        }
    }
}