export function createPhoneNumber(numbers: number[]): string {
    let phoneNumber:string = "(xxx) xxx-xxxx"
    
    for(let i=0; i<numbers.length; i++){
      phoneNumber = phoneNumber.replace("x", numbers[i].toString())
    }
      
    return phoneNumber
  }