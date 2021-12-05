const fs = require('fs');

const main = () => {
  const data: string = fs.readFileSync('input5_1.txt', 'utf8');
  const lines = data.split('\n').filter(line => line);

  const grid = {};
  for (const line of lines) {
    const [x, y] = line.split(" -> ");
    const [x1, y1] = x.split(",").map(x => parseInt(x)), [x2, y2] = y.split(",").map(y => parseInt(y));

    // only straight lines
    if (x1 === x2 || y1 === y2) {
      if (x1 === x2 && y1 === y2) {

        grid[`${x1},${y1}`] = (grid[`${x1},${y1}`] ?? 0) + 1;
      } else if (x1 === x2) {

        let lower = y1 < y2 ? y1 : y2;
        const higher = y1 > y2 ? y1 : y2;

        while (lower <= higher) {
          grid[`${x1},${lower}`] = (grid[`${x1},${lower}`] ?? 0) + 1;
          lower++;
        }
      } else /* if (y1 === y2)  */{
        let lower = x1 < x2 ? x1 : x2;
        const higher = x1 > x2 ? x1 : x2;

        while (lower <= higher) {
          grid[`${lower},${y1}`] = (grid[`${lower},${y1}`] ?? 0) + 1;
          lower++;
        }
      }
    }
  }

  let total2Plus = 0;
  for (const coord of Object.keys(grid)) {
    if (grid[coord] > 1) {
      total2Plus++;
    }
  }

  console.log(total2Plus);
}

main();