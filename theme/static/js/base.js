let is_dark_mode = null
const changeMode = async() => {
    try{
        const response = await fetch('http://127.0.0.1:8000/change/',{
            method:'POST',
                headers:{
                    'Content-Type': 'application/json',
                },
                credentials: 'same-origin',
            })
            if (response.ok) {
                const data = await response.json();
                is_dark_mode = data.is_dark_mode;
                const htmlElement = document.documentElement;
                const changeModeIcon = document.getElementById('change-mode-icon')
                changeModeIcon.classList.replace('fa-moon','fa-sun') ? is_dark_mode : changeModeIcon.classList.replace('fa-sun','fa-moon')
                htmlElement.classList.contains('dark') ? htmlElement.classList.remove('dark') && !is_dark_mode : htmlElement.classList.add('dark');
            } else {
                console.error('Failed to toggle dark mode');
            }
    }
    catch(err){
        console.error('Error:', err);
    }
}
const switchModeBtn = document.getElementById('change-mode')
switchModeBtn.addEventListener('click',changeMode)
