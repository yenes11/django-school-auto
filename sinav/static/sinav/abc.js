console.log("heloo")

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const sorusayisi = modalBtn.getAttribute('data-question')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3"> Başlamak istediğinize emin misiniz? </div>
        <div class="text-muted">
            <ul>
                <li>Sınav: <b>${name}</b></li>
                <li>Soru Sayısı: <b>${sorusayisi}</b></li>
                <li>Süre: <b>${time} dakika</b></li>
            </ul>
        </div>

    `
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))