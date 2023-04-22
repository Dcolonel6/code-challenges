export const isPangram = (phrase: string): boolean => { 
    return phrase.replaceAll(/[^A-Z]/gi,"").replaceAll(/(.)(?=.*\1)/gi, "").length === 26
}