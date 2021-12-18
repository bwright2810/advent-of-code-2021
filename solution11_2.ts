const fs = require('fs');

const main = () => {
  const data: string = fs.readFileSync('input11_1.txt', 'utf8');
  // const data: string = fs.readFileSync('testinput11_1.txt', 'utf8');
  const lines = data.split('\n').filter(line => line);

  const grid = [];
  lines.forEach((line, y) => grid.push(line.split('').map((digit, x) => {
     return { val: parseInt(digit), y, x };
  })));
  const gridTotalSize = grid.reduce((totalSize, row) => totalSize + row.length, 0);

  const step = (grid): boolean => {
    grid.forEach(row => row.forEach(octo => octo.val = octo.val + 1))

    const flashedThisStep = {};
    grid.forEach(row => row.forEach(octo => { if (octo.val > 9) flash(grid, flashedThisStep, octo) }));

    if (gridTotalSize === Object.keys(flashedThisStep).length) {
      return true;
    }
    
    grid.forEach(row => row.forEach(octo => { if (octo.val > 9) octo.val = 0 }));

    return false;
  }

  const flash = (grid, stepFlashMap, { y, x }) => {
    const octoKey = `${y},${x}`;
    if (stepFlashMap[octoKey]) {
      return;
    }

    stepFlashMap[octoKey] = true;
    const adjacentOctos = [
      grid[y - 1]?.[x - 1], grid[y - 1]?.[x], grid[y - 1]?.[x + 1],
      grid[y]?.[x - 1], grid[y]?.[x + 1],
      grid[y + 1]?.[x - 1], grid[y + 1]?.[x], grid[y + 1]?.[x + 1]
    ].filter (octo => octo);
    adjacentOctos.forEach(octo => octo.val = octo.val + 1);
    adjacentOctos.forEach(octo => { if (octo.val > 9) flash(grid, stepFlashMap, octo) });
  }

  for (let i = 0; i > -1; i++) {
    console.log(`Step ${i + 1}`);

    if (step(grid)) {
      console.log(`All flashed on step ${i + 1}`);
      break;
    }
  }
}

main();