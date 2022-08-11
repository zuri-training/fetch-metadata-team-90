const lessThan = document.querySelector('.less-than-button')
const greaterThan = document.querySelector('.greater-than-button')
const eliceps2 = document.querySelector('.btn-eliceps-2')
const button9 = document.querySelector('.btn-9')
const button10 = document.querySelector('.btn-10')
const button1 = document.querySelector('.btn-1')
const button2 = document.querySelector('.btn-2')
const eliceps1 = document.querySelector('.btn-eliceps-1')

let handleEvent = true

const handleClick = () => {
    if (handleEvent){
        return (
            eliceps2.setAttribute('class', 'display-none'),
            button9.setAttribute('class', ''),
            button10.setAttribute('class', ''),
            button1.setAttribute('class', 'display-none'),
            button2.setAttribute('class', 'display-none'),
            eliceps1.setAttribute('class', '')
        );
    };

}
const resetClick = () => {
    if(!handleEvent){
        return(
            eliceps1.setAttribute('class', 'btn-eliceps-1'),
            button9.setAttribute('class', 'display-none'),
            button10.setAttribute('class', 'display-none'),
            button1.setAttribute('class', ''),
            button2.setAttribute('class', ''),
            eliceps2.setAttribute('class', '')
        )
    }
}

greaterThan.addEventListener('click', ()=>{handleClick(), handleEvent=false})
lessThan.addEventListener('click', ()=>{resetClick(), handleEvent=true})
