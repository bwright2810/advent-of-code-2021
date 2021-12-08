const fs = require('fs');

const main = () => {
  const data: string = fs.readFileSync('input6_1.txt', 'utf8');
  const lines = data.split('\n').filter(line => line);

  const newFish = () => 8;
  const resurrect = () => [newFish(), 6];
  const processDay = (fish) => fish === 0 ? resurrect() : [--fish];
  
  // let fishes = lines[0].split(",").map(num => parseInt(num));
  let fishes = [3,4,3,1,2]

  let daysPassed = 0;
  while (daysPassed < 18) {
    console.log(`Day ${daysPassed}`);
    fishes = fishes.reduce((newFishes, fish) => newFishes.concat(processDay(fish)), []);
    daysPassed++;
  }

  console.log(fishes.length);
}

main();