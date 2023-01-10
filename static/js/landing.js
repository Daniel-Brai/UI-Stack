
const about = document.querySelector('#about')
const about_l = document.querySelector('#about_link')
const about_l2 = document.querySelector('#about_link2')
const feat = document.querySelector('#features')
const feat_l = document.querySelector('#feat_link')
const faq = document.querySelector('#faq')
const faq_l = document.querySelector('#faq_link')
const contact = document.querySelector('#contact')
const contact_l = document.querySelector('#contact_link')
const contact_l2 = document.querySelector('#contact_link2')
const forms = document.querySelectorAll('form')

about_l.addEventListener('click', () => {
    about.scrollIntoView({behaviour: "smooth"})
})
about_l2.addEventListener('click', () => {
    about.scrollIntoView({behaviour: "smooth"})
})
feat_l.addEventListener('click', () => {
    feat.scrollIntoView({behaviour: "smooth"})
})
faq_l.addEventListener('click', () => {
    faq.scrollIntoView({behaviour: "smooth"})
})
contact_l.addEventListener('click', () => {
    contact.scrollIntoView({behaviour: "smooth"})
})
contact_l2.addEventListener('click', () => {
    contact.scrollIntoView({behaviour: "smooth"})
})
// forms.forEach((form) => {
//     form.addEventListener('submit', (e) => {
//         e.preventDefault()
//     })
// })