/* eslint-disable */ //warning 제거
import { Table } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { addCount, minusCount, removeCart } from "../store.js";
import { changeName, increase } from "./../store/userSlice.js";


function Cart(){

  /* 2. Redux 사용하기 */
  /* store.js에서 가져오기 */
  let state = useSelector((state)=>{ return state }) //모든 state 가져옴
  //let userState = useSelector((state)=>{ return state.user }) // user state만 가져옴
  //let stockState = useSelector((state)=>{ return state.stock }) // stock state만 가져옴
  //let state = useSelector((state)=> state) //return과 {중괄호} 동시에 생략 가능

  /* 가져온거 사용하기 */
  //console.log(state.user) : user 사용하기
  //console.log(state.stock) : stock 사용하기

  let dispatch = useDispatch()

  return(
    <div>

      <h6>{ state.user.name } {state.user.age} 의 장바구니</h6>
      <button onClick={()=>{ dispatch(increase(100,10)) }}>버튼</button>

      <Table>
        <thead>
          <tr>
            <th>#</th>
            <th>상품명</th>
            <th>수량</th>
            <th>가격</th>
            <th>변경</th>
            <th>삭제</th>
          </tr>
        </thead>
        <tbody>
          {/* Redux로 장바구니 상품 가져오기 */}
          {
            state.cart.map((a,i)=>{
              return(
                <tr key={i}>
                  <td>{(i+1)}</td>
                  <td>{state.cart[i].name}</td>
                  <td>{state.cart[i].count}</td>
                  <td>구현해보기</td>
                  <td>
                    <button onClick={()=>{ dispatch(addCount(state.cart[i].id)) }}>+</button>
                    <button onClick={()=>{ dispatch(minusCount(state.cart[i].id)) }}>-</button>
                  </td>
                  <td>
                    <button onClick={()=>{ dispatch(removeCart(state.cart[i].id)) }}>×</button>
                  </td>
                </tr>
              )
            })
          }
        </tbody>
      </Table>

    </div>
  )
}

export default Cart