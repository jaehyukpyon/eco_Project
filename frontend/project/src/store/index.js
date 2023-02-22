import { createStore } from 'vuex'

export default createStore({
  state: {
    missionId: -1,
    stockName: '',
  },
  getters: {
    getMissionId(state) {
      return state.missionId;
    },
    getStockName(state) {
      return state.stockName;
    },
  },
  mutations: {
    setMissionId(state, payload) {
      state.missionId = payload;
    },
    setStockName(state, payload) {
      state.stockName = payload;
    }
  },
  actions: {
  },
  modules: {
  }
})
