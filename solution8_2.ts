const fs = require('fs');

const TWO_SEG = 1;
const THREE_SEG = 7;
const FOUR_SEG = 4;
const FIVE_SEG = [2, 3, 5];
const SIX_SEG = [0, 6, 9];
const SEVEN_SEG = 8;

enum Seg {
  T, TL, TR, M, BL, BR, B
}

const digitMap = {
  0: [Seg.T, Seg.TL, Seg.TR, Seg.BL, Seg.BR, Seg.B],
  1: [Seg.TR, Seg.BR],
  2: [Seg.T, Seg.TR, Seg.M, Seg.BL, Seg.B],
  3: [Seg.T, Seg.TR, Seg.M, Seg.BR, Seg.B],
  4: [Seg.TL, Seg.TR, Seg.M, Seg.BR],
  5: [Seg.T, Seg.TL, Seg.M, Seg.BR, Seg.B],
  6: [Seg.T, Seg.TL, Seg.M, Seg.BL, Seg.BR, Seg.B],
  7: [Seg.T, Seg.TR, Seg.BR],
  8: [Seg.T, Seg.TL, Seg.TR, Seg.M, Seg.BL, Seg.BR, Seg.B],
  9: [Seg.T, Seg.TL, Seg.TR, Seg.M, Seg.BR, Seg.B]
}

const main = () => {
  const data: string = fs.readFileSync('input8_1.txt', 'utf8');
  // const data: string = fs.readFileSync('testinput_8_2.txt', 'utf8');
  const lines = data.split('\n').filter(line => line);
  // const lines = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']

  let total = 0;
  for (const line of lines) {
    const [signalPart, digitPart] = line.split("|");
    const signals = signalPart.split(" ");
    const digits = digitPart.split(" ").filter(d => d);

    // const sigDigMap = {};
    const oneSig = signals.find(s => s.length === 2);
    // sigDigMap[oneSig] = 1;
    const sevenSig = signals.find(s => s.length === 3);
    // sigDigMap[sevenSig] = 7;
    const fourSig = signals.find(s => s.length === 4);
    // sigDigMap[fourSig] = 4;
    const eightSig = signals.find(s => s.length === 7);
    // sigDigMap[eightSig] = 8;

    let remSigs = signals.filter(s => ![oneSig, sevenSig, fourSig, eightSig].includes(s));

    let workingMap = { 
      0: [],
      1: [oneSig], 
      2: [],
      3: [],
      4: [fourSig],
      5: [],
      6: [],
      7: [sevenSig], 
      8: [eightSig],
      9: []
    };

    for (const sig of remSigs) {
      if (sig.length === 5) {
        FIVE_SEG.forEach(num => workingMap[num].push(sig));
      } else /* 6 */ {
        SIX_SEG.forEach(num => workingMap[num].push(sig));
      }
    }

    // while (Object.keys(workingMap).filter(num => workingMap[num].length !== 1).length > 0) {
      for (let i = 0; i < Object.keys(workingMap).length; i++) {
        if (workingMap[i].length === 1) continue;

        // const knownDigits = Object.keys(workingMap).filter(num => workingMap[num].length === 1);
        const knownDigits = [1, 4, 7, 8];

        const digitSegs = digitMap[i];
        let potentialSigs = workingMap[i];

        for (const potSig of potentialSigs) {
          let sigWorks = true;
          for (const knownDigit of knownDigits) {
            const knownDigitSegs = digitMap[knownDigit];
            const sharedSegsCt = digitSegs.filter(ds => knownDigitSegs.includes(ds)).length;
            const knownSig = workingMap[knownDigit][0];
            const sharedCharsCt = potSig.split('').filter(pc => {
              return knownSig.split('').includes(pc)
            }).length;
            if (sharedCharsCt !== sharedSegsCt) {
              sigWorks = false;
              break;
            }
          }
          if (!sigWorks) {
            workingMap[i] = workingMap[i].filter(sig => sig !== potSig);
            continue;
          }
        }
      }
    // }

    const sigToDigitMap = {};
    Object.keys(workingMap).forEach(key => {
      let sig: string = workingMap[key][0];
      sig = sig.split('').sort().join('');
      sigToDigitMap[sig] = key;
    });

    // console.log(JSON.stringify(sigToDigitMap));
    // console.log(digits.map(d => d.split('').sort().join('')));
    // console.log(parseInt(digits.map(ds => sigToDigitMap[ds.split('').sort().join('')]).join('')));

    const finalNum = parseInt(digits.map(ds => sigToDigitMap[ds.split('').sort().join('')]).join(''));
    total += finalNum;
  }  

  console.log(total);
}

main();