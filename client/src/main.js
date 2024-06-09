// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import FloatingVue from 'floating-vue'
import cors from 'cors'

import router from './router'

const app = createApp(App)
const corsOptions = {
    origin:'*', 
    credentials:true,            //access-control-allow-credentials:true
    optionSuccessStatus:200,
}

app.use(FloatingVue)
app.use(router)
app.mount('#app')

cors(corsOptions)
