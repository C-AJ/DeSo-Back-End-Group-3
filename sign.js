const EC = require('elliptic').ec;
const sha256 = require('sha256');

function seedHexToPrivateKey(seedHex) {
  const ec = new EC('secp256k1');
  return ec.keyFromPrivate(seedHex);
}

const uvarint64ToBuf = (uint) => {
  const result = [];

  while (uint >= 0x80) {
    result.push((uint & 0xff) | 0x80);
    uint >>>= 7;
  }

  result.push(uint | 0);

  return new Buffer.from(result);
};


function signTransaction() {
  const seedHex = "3f68110f271593c3c955ffa41545933a3188d4bb13ecd6e2b545cf917f925abe"
  const transactionHex = "0144fcc611e3a90a065de1cdf329e7fcf42cc7d11977b1f27254ad36b5764556450001036276d125b46fe0a65c9edbd41056334b15d78c3f54fe494d81db993416ee482b929ff09e0405380000277b22426f6479223a2273656e70616920706c73206e6f746963656565656565656531313131227de807d4619ae29b9b8b81a1f7160021036276d125b46fe0a65c9edbd41056334b15d78c3f54fe494d81db993416ee482b0000"

  const privateKey = seedHexToPrivateKey(seedHex);

  const transactionBytes = new Buffer.from(transactionHex, 'hex');
  const transactionHash = new Buffer.from(sha256.x2(transactionBytes), 'hex');
  const signature = privateKey.sign(transactionHash);
  const signatureBytes = new Buffer.from(signature.toDER());
  const signatureLength = uvarint64ToBuf(signatureBytes.length);

  const signedTransactionBytes = Buffer.concat([
    transactionBytes.slice(0, -1),
    signatureLength,
    signatureBytes,
  ]);

  return signedTransactionBytes.toString('hex');
}

x = signTransaction();
console.log(x)