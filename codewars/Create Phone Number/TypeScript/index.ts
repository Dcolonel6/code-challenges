export function createPhoneNumber(numbers: number[]): string {
    return `(${numbers.slice(0,3).join("")}) ${numbers.slice(3,6).join("")}-${numbers.slice(6).join("")}`
}