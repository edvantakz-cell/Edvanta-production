const API = "https://your-backend-url.railway.app"

function register(){
fetch(API + "/register",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
full_name: full_name.value,
birth_date: birth_date.value,
email: email.value,
password: password.value
})
})
.then(r=>r.json()).then(d=>alert(d.message))
}

function login(){
fetch(API + "/login",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
email: login_email.value,
password: login_password.value
})
})
.then(r=>r.json())
.then(d=>{
localStorage.setItem("token", d.token)
window.location="dashboard.html"
})
}

function generate(){
fetch(API + "/generate",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
user_id:1,
class_name: class_name.value,
subject: subject.value,
topic: topic.value,
lesson_type: sor.checked ? "СОР/СОЧ" : "Обычный урок",
extra_prompt: extra_prompt.value
})
})
.then(r=>r.json())
.then(d=>{
result.innerHTML = `
<p>Документ: ${d.lesson_doc}</p>
<p>Презентация: ${d.presentation}</p>
`
})
}

function subscribe(){
alert("Оплата 5000 тг. (Интеграция Halyk позже)")
}

function logout(){
localStorage.removeItem("token")
window.location="index.html"
}