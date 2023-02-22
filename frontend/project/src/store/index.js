import { createStore } from 'vuex'

export default createStore({
  state: {
    missionId: -1,
  },
  getters: {
    getMissionId(state) {
      return state.missionId;
    },
  },
  mutations: {
    setMissionId(state, payload) {
      state.missionId = payload;
    }
  },
  actions: {
  },
  modules: {
  }
})
