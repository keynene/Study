import { configureStore, createSlice } from "@reduxjs/toolkit";

/* state만들기 */
let 작명 = createSlice({
  name : 'state이름',
  initialState : '값'
})

//useState 역할
let user = createSlice({
  name : 'user',
  initialState : 'noi'
})

let stock = createSlice({
  name : 'stock',
  initialState : [10,11,12]
})

let cartProduct = createSlice({
  name : 'cartProduct',
  initialState : [
    {id : 0, name : 'White and Black', count : 2},
    {id : 2, name : 'Grey Yordan', count : 1}
  ] 
})

export default configureStore({
  reducer:{
    /* state등록하기 */
    //여기 등록하면 모든 컴포넌트들이 state 사용 가능
    작명 : 작명.reducer,


    user : user.reducer,
    stock : stock.reducer,
    cartProduct : cartProduct.reducer
  }
})