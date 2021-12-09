const fs = require('fs');

const main = () => {
  const data: string = fs.readFileSync('input7_1.txt', 'utf8');
  const lines = data.split('\n').filter(line => line);
  const line = lines[0];
  // const line = "16,1,2,0,4,2,7,1,2,14";

  const origPositions = line.split(',').map(pos => parseInt(pos));

  let [highest, lowest] = [null, null];
  origPositions.forEach(pos => {
    if (highest === null) {
      highest = pos;
    }
    if (lowest === null) {
      lowest = pos;
    }

    if (pos > highest) {
      highest = pos;
    }
    if (pos < lowest) {
      lowest = pos;
    }
  });

  console.log(`Highest position: ${highest}`);
  console.log(`Lowest position: ${lowest}`);

  let lowestFuelCost = null;

  const memoMap = {};
  const memoCost = function memoCost(num) {
    // console.log("MEMO COST NUM: "+ num);
    if (num === 1 || num === 0) {
      return num;
    } else {
      const memoizedVal = memoMap[num];
      const val = memoizedVal ? memoizedVal : num + memoCost(num - 1);
      if (!memoizedVal) {
        memoMap[num] = val;
      }
      return val;
      // let totalCost = 0;
      // let curr = num;
      // while (curr !== 1) {
      //   const memoizedVal = memoMap[num];
      //   if (memoizedVal) {
      //     totalCost += memoizedVal;
      //     curr = 0;
      //   } else {
      //     totalCost += curr;
      //     curr--;
      //   }
      // }
    }
  }
  
  for (let i = lowest; i < highest + 1; i++) {
    console.log(`Checking position ${i}`);
    let totalFuelCost = 0;
    for (const pos of origPositions) {
      // console.log("CURRENT POS");
      const diff = Math.abs(i - pos);
      const cost = memoCost(diff);
      totalFuelCost += cost;
    }
    if (lowestFuelCost === null || totalFuelCost < lowestFuelCost) {
      lowestFuelCost = totalFuelCost;
    }
  }

  console.log("LOW FUEL COST");
  console.log(lowestFuelCost);
}

main();