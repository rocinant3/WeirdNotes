import alertStore from '$lib/stores/alert'

const warning = (message: string) => {
  alertStore.set({level: "warning", message})
}


const info = (message: string) => {
  alertStore.set({level: "info", message})
}


const success = (message: string) => {
  alertStore.set({level: "success", message})
}

const clear = () => {
  alertStore.set({level: "default", message: ""})
}


const alertService = {info, warning, success, clear}

export default alertService;
