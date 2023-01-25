function convertBinary(N){
    //convert to  binary
  const binary = N.toString(2)
  
  //grab all the zeros between the ones
  try{
    const matchedArray = [...binary.match(/(?<=1)0{1,}(?=1)/g)]
    return Math.max(...matchedArray.map(matchedStr => matchedStr.length))
  }catch(e){
    return 0
  }
  
}