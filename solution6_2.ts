const fs = require('fs');

const main = () => {
  const data: string = fs.readFileSync('input6_1.txt', 'utf8');
  const lines = data.split('\n').filter(line => line);
  
  let map = [0, 0, 0, 0, 0, 0, 0, 0, 0];
  let fishes = lines[0].split(",").map(num => parseInt(num));
  fishes.forEach(fish => {
    map[fish] = ++map[fish];
  });
  // let map = [0, 1, 1, 2, 1, 0 , 0 ,0 ,0]
  let daysPassed = 0;
  while (daysPassed < 256) {
    console.log(`Day ${daysPassed}`);
    
    const newMap = [0, 0, 0, 0, 0, 0, 0, 0];
    for (let i = 0; i < map.length; i++) {
      if (i === 0) {
        newMap[8] = map[i];
        newMap[6] = map[i];
      } else {
        newMap[i - 1] = newMap[i - 1] + map[i];
      }
    }
    map = newMap;

    daysPassed++
  }

  console.log(map);
  const total = map.reduce((prev, num) => prev + num, 0);
  console.log(total);
}

main();