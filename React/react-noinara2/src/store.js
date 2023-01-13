/* eslint-disable */ //warning 제거
import { configureStore, createSlice } from "@reduxjs/toolkit";
import user from "./store/userSlice";

/* state만들기 */
let 작명 = createSlice({
  name : 'state이름',
  initialState : '값'
}) 


let stock = createSlice({
  name : 'stock',
  initialState : [10,11,12]
})

let cart = createSlice({
  name : 'cart',
  initialState : [
    {id : 0, name : 'White and Black', count : 2},
    {id : 2, name : 'Grey Yordan', count : 1}
  ],

  reducers : {
    addCount(state, action){
      //x는 findIndex가 적용되는 arr의 하나하나의 데이터. 지금 여기선 객체 하나하나를 뜻 함 {},{}
      let index = state.findIndex((x)=> x.id == action.payload )
      state[index].count ++
      
      /*아래와 같이 꼭 구현해보기 (addCount, minusCount로 안쪼개고 Count함수 안에 +,- 다 구현하기)
      if (change.payload == true){
        state[index].count++
      } else if (change.payload == false){
        state[index].count--
      }
      */
    },
    minusCount(state, action){
      let index = state.findIndex((x)=> x.id == action.payload )
      if (state[index].count > 1){
        state[index].count --
      }
      else {
        if(confirm("🤷🏻‍♀️ 장바구니에서 상품을 삭제할까요?")){
          state.splice(index,1)
        }
      }
    },

    addCart(state, action){
      let comp = state.findIndex((x)=> x.name == action.payload.title )
      //상품이 중복되지않으면 추가
      if (comp == -1){
        state.push({id : action.payload.id, name : action.payload.title, count : 1})
      }
      //상품이 중복되었으면 경고창
      else {
        if(confirm("🙅🏻‍♀️ 이미 상품이 장바구니에 "+ state[comp].count +"개 있습니다! 수량을 추가할까요?")){
          state[comp].count++
        }
      }
    },
    
    removeCart(state, action){
      let index = state.findIndex((x)=> x.id == action.payload )
      state.splice(index,1)
      
    }
  }
})


export let { addCount, minusCount, addCart, removeCart } = cart.actions

export default configureStore({
  reducer:{
    /* state등록하기 */
    //여기 등록하면 모든 컴포넌트들이 state 사용 가능
    작명 : 작명.reducer,


    user : user.reducer,
    stock : stock.reducer,
    cart : cart.reducer,
  }
})