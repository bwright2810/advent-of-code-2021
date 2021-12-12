const fs = require('fs');

const TWO_SEG = 1;
const THREE_SEG = 7;
const FOUR_SEG = 4;
const SEVEN_SEG = 8;

const main = () => {
  const data: string = fs.readFileSync('input8_1.txt', 'utf8');
  const lines = data.split('\n').filter(line => line);

  let uniqueDigitCount = 0;
  for (const line of lines) {
    const [signalPart, digitPart] = line.split("|");
    const signals = signalPart.split(" ");
    const digits = digitPart.split(" ");

    // const singleSig = signals.find(s => s.length === 1);
    // const threeSig = signals.find(s => s.length === 3);
    // const fourSig = signals.find(s => s.length === 4);
    // const fiveSig = signals.find(s => s.length === 8);

    for (const digit of digits) {
      // if ([singleSig, threeSig, fourSig, fiveSig].includes(digit)) {
      //   uniqueDigitCount++;
      // }
      if ([2, 3, 4, 7].includes(digit.length)) {
        uniqueDigitCount++;
      }
    }
  }  

  console.log(uniqueDigitCount);
}

main();