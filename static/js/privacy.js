const contact = document.querySelector('#contact_block')
const contact_l = document.querySelector('#contact_link')

contact_l.addEventListener('click', () => {
    contact.scrollIntoView({behaviour: "smooth"})
})
