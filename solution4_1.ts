const fs = require('fs');

const main = () => {
  const data: string = fs.readFileSync('input4_1.txt', 'utf8');
  const lines = data.split('\n');

  const drawnNumbers = lines[0].split(',').map(line => parseInt(line));
  const boardLines = lines.slice(1);

  // parse boards into a structure
  let doingBoard = false;
  const boardArrays = [];
  let arrIdx = 0;
  for (const line of boardLines) {
    if (!doingBoard && !line) {
      continue;
    } else if (doingBoard && !line) {
      doingBoard = false;
      arrIdx++;
    } else {
      if (!doingBoard) {
        doingBoard = true;
        boardArrays.push([]);
      }
      boardArrays[arrIdx].push(line);
    }
  }

  const boards = [];
  for (const boardArr of boardArrays) {
    const board = {};
    for (let i = 0; i < (boardArr as []).length; i++) {
      const line = boardArr[i];
      const numbers = line.split(" ").filter(l => l)
        .map(num => { return { marked: false, val: parseInt(num) } });
      board[i] = numbers;
    }
    boards.push(board);
  }

  // for (const board of boards) {
  //   for (let i = 0; i < Object.keys(board).length; i++) {
  //     console.log(board[i]);
  //   }
  // }

  // create function to mark boards
  const markBoard = (board, drawn: number) => {
    for (let i = 0; i < Object.keys(board).length; i++) {
      for (let j = 0; j < board[i].length; j++) {
        if (drawn === board[i][j].val) {
          board[i][j].marked = true;
          return;
        }
      }
    }
  }

  // let board = boards[0];
  // for (let i = 0; i < Object.keys(board).length; i++) {
  //   for (let j = 0; j < board[i].length; j++) {
  //     console.log(`${board[i][j].val}: ${board[i][j].marked}`)
  //   }
  // }

  // create function to check if board is complete
  const isAllMarked = (board, yCoords, xCoords) => yCoords.every((yc, idx) => board[yc][xCoords[idx]].marked);

  // console.log(isAllMarked(boards[0], [0, 4, 0], [0, 4, 3]));

  const checkWin = (board) => {
    let paths = []; // each path is an array with two arrays
    for (let y = 0; y < Object.keys(board).length; y++) {
      const rowPath = [[], []];
      for (let x = 0; x < board[y].length; x++) {
        rowPath[0].push(y);
        rowPath[1].push(x);
      }
      paths.push(rowPath);
    }

    for (let x = 0; x < board[0].length; x++) {
      const colPath = [[], []];
      for (let y = 0; y < Object.keys(board).length; y++) {
        colPath[0].push(y);
        colPath[1].push(x);
      }
      paths.push(colPath);
    }

    return paths.some(path => isAllMarked(board, path[0], path[1]));
  }

  // determine final score
  const score = (board, lastNum) => {
    let unmarkedScore = 0;
    for (let y = 0; y < Object.keys(board).length; y++) {
      for (const num of board[y]) {
        if (!num.marked) {
          unmarkedScore += num.val;
        }
      }
    }
    return unmarkedScore * lastNum;
  }

  for (const drawn of drawnNumbers) {
    boards.forEach(board => markBoard(board, drawn));
    const winner = boards.find(board => checkWin(board));

    if (winner) {
      console.log("WINNER");
      console.log("SCORE:");
      console.log(score(winner, drawn));
      break;
    }
  }
};

main();