//// ========================================================
////                     Iteration 1
//// ========================================================
//// originally calls images, i want to call numbers.
////  original is commented
////     function preload() {
////        tiles[0] = loadImage("blank.png");
////         tiles[0] = loadImage("up.png");
////         tiles[0] = loadImage("right.png");
////         tiles[0] = loadImage("down.png");
////          }

////  tried using
////      tiles[0] = ' ';
////      tiles[1] = '1';
////  didnt seem to work so have instead created pngs in figma.

// const tiles = [];

// function preload() {
//     tiles[0] = loadImage("tiles/Untitled.png");
//     tiles[1] = loadImage("tiles/1.png");
//     tiles[2] = loadImage("tiles/2.png");
//     tiles[3] = loadImage("tiles/3.png");
//     tiles[4] = loadImage("tiles/4.png");
//     tiles[5] = loadImage("tiles/5.png");
//     tiles[6] = loadImage("tiles/6.png");
//     tiles[7] = loadImage("tiles/7.png");
//     tiles[8] = loadImage("tiles/8.png");
//     tiles[9] = loadImage("tiles/9.png");
// }

// function setup() {
//     createCanvas(400, 400);
// }

// function draw() {
//     background(0);
//     Image(tiles[0], 0, 0);
//     Image(tiles[1], 50, 0);
//     Image(tiles[2], 100, 0);
//     Image(tiles[3], 150, 0);
//     Image(tiles[4], 0, 50);
// }

//// didnt work was asking for 'node' which i understood as node.js.
//// downloaded node, did not return visual output.
//// downloaded p5.vscode extension by Sam Lavigne.
//// works but does not display tile images yet. its a pretty awesome extension, when creating a new p5 project it creates a .html, .css, json and .js file which is then displayed in browser via a private server (the details of which im unsure of, though could be interesting to look into in the future)

//// ========================================================
////                     Iteration 2
////========================================================

// const tiles = [];

// function preload() {
//     tiles[0] = loadImage("tiles/Untitled.png");
//     tiles[1] = loadImage("tiles/1.png");
//     tiles[2] = loadImage("tiles/2.png");
//     tiles[3] = loadImage("tiles/3.png");
//     tiles[4] = loadImage("tiles/4.png");
//     tiles[5] = loadImage("tiles/5.png");
//     tiles[6] = loadImage("tiles/6.png");
//     tiles[7] = loadImage("tiles/7.png");
//     tiles[8] = loadImage("tiles/8.png");
//     tiles[9] = loadImage("tiles/9.png");
// }

// function setup() {
//     createCanvas(400, 400);
// }

// function draw() {
//     background(151);
//     image(tiles[0], 0, 0);
//     image(tiles[1], 50, 0);
//     image(tiles[2], 100, 0);
//     image(tiles[3], 150, 0);
//     image(tiles[4], 0, 50);
    

// }

////  Uncaught TypeError: Image constructor: 'new' is required
////      draw http://127.0.0.1:5500/myCodeStudies/WFC/WFC.js:76
////      redraw http://127.0.0.1:5500/myCodeStudies/WFC/libraries/p5.min.js:3
////      _draw http://127.0.0.1:5500/myCodeStudies/WFC/libraries/p5.min.js:3
////  Ive downloaded p5.js from their website, copied the libraries over to WFC/libraries and will re try
//// GOT IT.. theres a difference between 'image' and 'Image'.
//// lower case is what I needed and is a function that draws the image mentioned, 'image(Image, x, y)' is the typical layout but other parameters may be passed.
//// upper case is a variable to declare an image
//// now that its working ive got up to the point where we look at declaring what tile can be a valid neighbour to other tile. Its become clear that this version of WFC wouldnt allow for a sudoku to be made (but would allow for a solver) as the numbers (or tiles) can be placed next to each other but only when certain checks are passed, this is not how I understand WFC to work.. though im open to being wrong

// //// ========================================================
// ////                     Iteration 3
// ////========================================================

// //  Its become difficult to follow along using numbers instead of 'puzzle piece' images so i am changing the tile images
// // declaring 'tiles' as an array and a constant (constant means that the variable (tiles[]) cannot be redeclared. as an array however its contents can be edited. A constant named 'tiles' can still be declared within a function as constants have block scope (is unique to the block think of a block as an html <div>)
// const tiles = []; 

// const grid = [];

// // will be used for 'dimensions'
// const DIM = 2; 

// const BLANK = 0;
// const UP = 1;
// const RIGHT = 2;
// const DOWN = 3;
// const LEFT = 4;

// // preload images for ease of use, these images have been preloaded into the array previously made
// function preload() { 
//     tiles[0] = loadImage("tiles/BLANK.png");
//     tiles[1] = loadImage("tiles/UP.png");
//     tiles[2] = loadImage("tiles/RIGHT.png");
//     tiles[3] = loadImage("tiles/DOWN.png");
//     tiles[4] = loadImage("tiles/LEFT.png");
// }

// // creates the canvas.
// // 
// function setup() {
//     createCanvas(400, 400);

//     for (let i = 0; i < DIM*DIM; i++) {
//         grid[i] = {
//             collapsed: false,
//             options: [BLANK, UP, RIGHT, DOWN, LEFT],
//         };
//     }
//     // a 'manual collapse' to test that the 'draw' function works
//     grid[0].collapsed = true;
//     grid[0].options = [UP];
// }

// //  Image test removed,
// //  draw it if its been collapsed
// // NOTE: following along im not enjoying the way indentations are done here perhaps this can be incorporated into my own 'principals', it may also just be rules associated with writing in java script
// function draw() {
//     background(151);

//     const w = width / DIM; // works out the width and height of every cell on the grid thats (total width of the canvas/how many columns and rows there are(if DIM = 2 its 2 cells by 2 cells)
//     const h = height / DIM;
//     // count through every row and every column..
//     for (let j = 0; j < DIM; j++) {
//         for (let i = 0; i < DIM; i++) {
//             let cell = grid[i + j * DIM]; //.. find the index into that one dimensional grid array (see vid on pixel array)
//             if (cell.collapsed) { // if its been collpased only one option left,..
//                 let index = cell.options[0];
//                 image(tiles[index], i * w, j * h, w, h); // ..find the correct image and draw it
//             }   else { // other wise just draw a blank rectangle
//                 fill(0);
//                 stroke(255);
//                 rect(i * w, j* h, w, h);
//             }
//         }
//     }
    
// }

// //// ========================================================
// ////                     Iteration 3
// ////========================================================

// const tiles = []; 

// const grid = [];

// const DIM = 2; 

// const BLANK = 0;
// const UP = 1;
// const RIGHT = 2;
// const DOWN = 3;
// const LEFT = 4;

// function preload() { 
//     tiles[0] = loadImage("tiles/BLANK.png");
//     tiles[1] = loadImage("tiles/UP.png");
//     tiles[2] = loadImage("tiles/RIGHT.png");
//     tiles[3] = loadImage("tiles/DOWN.png");
//     tiles[4] = loadImage("tiles/LEFT.png");
// }


// function setup() {
//     createCanvas(400, 400);

//     for (let i = 0; i < DIM*DIM; i++) {
//         grid[i] = {
//             collapsed: false,
//             options: [BLANK, UP, RIGHT, DOWN, LEFT],
//         };
//     }
// }

// function draw() {
//     background(151);

//     // Picking cell with the least entropy
//     // NOTE: we have const variables and we have arrays( options[]) that point to those vars?obj?. we can have multiple arrays with those vars in different orders.

//     const gridCopy = grid.slice()
//     gridCopy.sort((a, b) => {
//         return a.options.length - b.options.length;
//     });

   

//     // len = the first elements ( 0 / [0]) length of options in the gridCopy array
//     // stopIndex starts at 0
//     // i = 1, if i is less than than the number of options in gridCopy than increase the value of i, if the length of options available in that element of the array is greater than len..
//     // ..log that value (of i) save it as that elements stopIndex then exit/break
//     let len = gridCopy[0].options.length;
//     let stopIndex = 0;
//     for (let i = 1; i < gridCopy.length; i++) {
//         if (gridCopy[i].options.length > len) {
//             stopIndex = i;
//             break;
//         }
//     }

//     // from gridCopy remove the value of stopIndex (if i = 2 the first two elements will be removed)
//     // cell = a random remaining element from the gridCopy array
//     // cells' collapsed attribute is now true
//     // pick = a random element option from from that cells remaining options
//     // cell.options now only contains the value of pick (for example DOWN from the remaining 2 options)
//     if(stopIndex > 0) gridCopy.splice(stopIndex);
//     const cell = random(gridCopy);
//     cell.collapsed = true;
//     const pick = random(cell.options);
//     cell.options = [pick]




//     console.log(grid);
//     console.log(gridCopy);

//     const w = width / DIM; 
//     const h = height / DIM;
//     for (let j = 0; j < DIM; j++) {
//         for (let i = 0; i < DIM; i++) {
//             let cell = grid[i + j * DIM];
//             if (cell.collapsed) {
//                 let index = cell.options[0];
//                 image(tiles[index], i * w, j * h, w, h); 
//             }   else {
//                 fill(0);
//                 stroke(255);
//                 rect(i * w, j* h, w, h);
//             }
//         }
//     }

//     noLoop();
    
// }

// //// ========================================================
// ////                     Iteration 4
// ////========================================================
// // lots of errors from the video were ammended here and notes will be put down in reflection for error checking.
// // the changes made in this section are mostly because of incorrect naming 

// const tiles = []; 

// let grid = [];
// const DIM = 2; 

// const BLANK = 0;
// const UP = 1;
// const RIGHT = 2;
// const DOWN = 3;
// const LEFT = 4;

// // instructions for what tiles can go next to what
// // 'rules' is an array object..
// // ..containing many values..
// // ..that contain arrays within themselves
// // 'array.element.array.value'

// // i thought at the time (and it was later mentioned in the video) that it would be better to describe the sides as having a value and that the tiles can only connect to a side with matching value..
// // if tile 1 has a right side with value of 1 then tile 2 with a left side value of 1 could also connect to it

// const rules = [
//     //blank
//     [
//         [BLANK, UP],
//         [BLANK, RIGHT],
//         [BLANK, DOWN],
//         [BLANK, LEFT],
//     ],
//     //up
//     [
//         [RIGHT, LEFT, DOWN],
//         [LEFT, UP, DOWN],
//         [BLANK, DOWN],
//         [RIGHT, UP, DOWN],
//     ],
//     //right
//     [
//         [RIGHT, LEFT, DOWN],
//         [LEFT, UP, DOWN],
//         [RIGHT, LEFT, UP],
//         [BLANK, LEFT]
//     ],
//     //down
//     [
//         [BLANK, UP],
//         [LEFT, UP, DOWN],
//         [RIGHT, LEFT, UP],
//         [RIGHT, UP, DOWN]
//     ],
//     //left
//     [
//         [RIGHT, LEFT, DOWN],
//         [BLANK, RIGHT],
//         [RIGHT, LEFT, UP],
//         [UP, DOWN, RIGHT],
//     ],
// ];

// function preload() { 
//     tiles[0] = loadImage("tiles/BLANK.png");
//     tiles[1] = loadImage("tiles/UP.png");
//     tiles[2] = loadImage("tiles/RIGHT.png");
//     tiles[3] = loadImage("tiles/DOWN.png");
//     tiles[4] = loadImage("tiles/LEFT.png");
// }


// function setup() {
//     createCanvas(400, 400);

//     for (let i = 0; i < DIM*DIM; i++) {
//         grid[i] = {
//             collapsed: false,
//             options: [BLANK, UP, RIGHT, DOWN, LEFT],
//         };
//     }
//     console.log(grid)
// }

// function checkValid(arr, valid) {
//     for (let i = arr.length - 1; i >= 0; i--) {
//         let element = arr[i];
//         if (!valid.includes(element)) {
//             arr.splice(i, 1);
//         }
//     }

// }

// function mousePressed() {
//     redraw();
// }

// function draw() {
//     background(151);
//     let gridCopy = grid.slice();
//     console.log(gridCopy)
//     gridCopy = gridCopy.filter((a) => !a.collapsed);
//     console.log(grid)
//     console.log(gridCopy)

//     gridCopy.sort((a, b) => {
//         return a.options.length - b.options.length;
//     });

//     let len = gridCopy[0].options.length;
//     let stopIndex = 0;
//     for (let i = 1; i < gridCopy.length; i++) {
//         if (gridCopy[i].options.length > len) {
//             stopIndex = i;
//             break;
//         }
//     }

//     if(stopIndex > 0) gridCopy.splice(stopIndex);
//     const cell = random(gridCopy);
//     cell.collapsed = true;
//     const pick = random(cell.options);
//     cell.options = [pick]


//     const w = width / DIM; 
//     const h = height / DIM;
//     for (let j = 0; j < DIM; j++) {
//         for (let i = 0; i < DIM; i++) {
//             let cell = grid[i + j * DIM];
//             if (cell.collapsed) {
//                 let index = cell.options[0];
//                 image(tiles[index], i * w, j * h, w, h); 
//             }   else {
//                 fill(0);
//                 stroke(255);
//                 rect(i * w, j* h, w, h);
//             }
//         }
//     }

//     // re-evaluate surrounding tiles and reduce entropy
//     const nextGrid = [];
//     for (let j = 0; j < DIM; j++) {
//         for (let i = 0; i < DIM; i++) {
//             let index = i + j * DIM;
//             // if collapsed do nothing its picked. otherwise..
//             if (grid[index].collapsed) { 
//                 nextGrid[index] = grid[index];
//             }  else {
//                 let options = [BLANK, UP, RIGHT, DOWN, LEFT];

//                 //..look up
//                 //look at the tile above me, only if im not in the first row
//                 if (j > 0) {  
//                     let up = grid[i + (j - 1) * DIM];
//                     let validOptions = [];
//                     for (let option of up.options) {
//                         let valid = rules[option] [2];
//                         validOptions = validOptions.concat(valid);
//                     }
//                     checkValid(options, validOptions);

//                 }
//                 //look right
//                 if (i < DIM - 1) {  
//                     let right = grid[i + 1 + j * DIM];
//                     let validOptions = [];
//                     for (let option of right.options) {
//                         let valid = rules[option] [3];
//                         validOptions = validOptions.concat(valid);
//                     }
//                     checkValid(options, validOptions);

//                 }
//                 // look down
//                 if (j < DIM - 1) {  
//                     let down = grid[i + (j + 1) * DIM];
//                     let validOptions = [];
//                     for (let option of down.options) {
//                         let valid = rules[option] [0];
//                         validOptions = validOptions.concat(valid);
//                     }
//                     checkValid(options, validOptions);

//                 }
//                 //look left
//                 if (i > 0) {  
//                     let left = grid[i - 1 + j * DIM];
//                     let validOptions = [];
//                     for (let option of left.options) {
//                         let valid = rules[option] [1];
//                         validOptions = validOptions.concat(valid);
//                     }
//                     checkValid(options, validOptions);
//                 }
             

//                 // options updated
//                 nextGrid[index] = {
//                     options,
//                     collapsed: false
//                 };
//             }
//         }
//     }

//     grid = nextGrid;
                
         

//     noLoop();
    
// }
//// ========================================================
////                     Iteration 5
////========================================================
// cloned the images used in video from github

const tiles = []; 

let grid = [];
const DIM = 8; 

const BLANK = 0;
const UP = 1;
const RIGHT = 2;
const DOWN = 3;
const LEFT = 4;

const rules = [
    //blank
    [
        [BLANK, UP],
        [BLANK, RIGHT],
        [BLANK, DOWN],
        [BLANK, LEFT],
    ],
    //up
    [
        [RIGHT, LEFT, DOWN],
        [LEFT, UP, DOWN],
        [BLANK, DOWN],
        [RIGHT, UP, DOWN],
    ],
    //right
    [
        [RIGHT, LEFT, DOWN],
        [LEFT, UP, DOWN],
        [RIGHT, LEFT, UP],
        [BLANK, LEFT]
    ],
    //down
    [
        [BLANK, UP],
        [LEFT, UP, DOWN],
        [RIGHT, LEFT, UP],
        [RIGHT, UP, DOWN]
    ],
    //left
    [
        [RIGHT, LEFT, DOWN],
        [BLANK, RIGHT],
        [RIGHT, LEFT, UP],
        [UP, DOWN, RIGHT],
    ],
];

function preload() { 
    tiles[0] = loadImage("tiles/demo/BLANK.png");
    tiles[1] = loadImage("tiles/demo/UP.png");
    tiles[2] = loadImage("tiles/demo/RIGHT.png");
    tiles[3] = loadImage("tiles/demo/DOWN.png");
    tiles[4] = loadImage("tiles/demo/LEFT.png");
}


function setup() {
    createCanvas(400, 400);

    for (let i = 0; i < DIM*DIM; i++) {
        grid[i] = {
            collapsed: false,
            options: [BLANK, UP, RIGHT, DOWN, LEFT],
        };
    }
    console.log(grid)
}

function checkValid(arr, valid) {
    for (let i = arr.length - 1; i >= 0; i--) {
        let element = arr[i];
        if (!valid.includes(element)) {
            arr.splice(i, 1);
        }
    }

}

function mousePressed() {
    redraw();
}

// order changed
// draw everything first and then if everything has been collapsed 'return'
function draw() {
    background(151);
    

    const w = width / DIM; 
    const h = height / DIM;
    for (let j = 0; j < DIM; j++) {
        for (let i = 0; i < DIM; i++) {
            let cell = grid[i + j * DIM];
            if (cell.collapsed) {
                let index = cell.options[0];
                image(tiles[index], i * w, j * h, w, h); 
            }   else {
                fill(0);
                stroke(255);
                rect(i * w, j* h, w, h);
            }
        }
    }

    let gridCopy = grid.slice();
    console.log(gridCopy)
    gridCopy = gridCopy.filter((a) => !a.collapsed);
    // console.log(grid)
    // console.log(gridCopy)

    if (gridCopy.length == 0) {
        return;
    }

    gridCopy.sort((a, b) => {
        return a.options.length - b.options.length;
    });

    let len = gridCopy[0].options.length;
    let stopIndex = 0;
    for (let i = 1; i < gridCopy.length; i++) {
        if (gridCopy[i].options.length > len) {
            stopIndex = i;
            break;
        }
    }

    if(stopIndex > 0) gridCopy.splice(stopIndex);
    const cell = random(gridCopy);
    cell.collapsed = true;
    const pick = random(cell.options);
    cell.options = [pick]


    const nextGrid = [];
    for (let j = 0; j < DIM; j++) {
        for (let i = 0; i < DIM; i++) {
            let index = i + j * DIM;
            if (grid[index].collapsed) { 
                nextGrid[index] = grid[index];
            }  else {
                let options = [BLANK, UP, RIGHT, DOWN, LEFT];

                //..look up
                if (j > 0) {  
                    let up = grid[i + (j - 1) * DIM];
                    let validOptions = [];
                    for (let option of up.options) {
                        let valid = rules[option] [2];
                        validOptions = validOptions.concat(valid);
                    }
                    checkValid(options, validOptions);

                }
                //look right
                if (i < DIM - 1) {  
                    let right = grid[i + 1 + j * DIM];
                    let validOptions = [];
                    for (let option of right.options) {
                        let valid = rules[option] [3];
                        validOptions = validOptions.concat(valid);
                    }
                    checkValid(options, validOptions);

                }
                // look down
                if (j < DIM - 1) {  
                    let down = grid[i + (j + 1) * DIM];
                    let validOptions = [];
                    for (let option of down.options) {
                        let valid = rules[option] [0];
                        validOptions = validOptions.concat(valid);
                    }
                    checkValid(options, validOptions);

                }
                //look left
                if (i > 0) {  
                    let left = grid[i - 1 + j * DIM];
                    let validOptions = [];
                    for (let option of left.options) {
                        let valid = rules[option] [1];
                        validOptions = validOptions.concat(valid);
                    }
                    checkValid(options, validOptions);
                }
             

                nextGrid[index] = {
                    options,
                    collapsed: false
                };
            }
        }
    }

    grid = nextGrid;
                
         

    // noLoop();
    
}
