import { createSlice } from "@reduxjs/toolkit"

//useState 역할
let user = createSlice({
  name : 'user',
  initialState : { name : 'noi', age : 28 },

  reducers : {
    changeName(state){ //기존state를 뜻함. 작명은 마음대로 (함수 사용할 때는 입력하지 않음)
      state.name = 'keynene'
    },
    increase(state, action){ //두 번째 파라미터부터 함수 호출 시 입력해야함  ex. increase(10)
      state.age += action.payload
    }
  }
})

//state수정하는 함수 export하기 (user는 userSlice.js에 있음)
export let { changeName, increase } = user.actions

export default user