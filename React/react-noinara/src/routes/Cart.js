import { Table } from "react-bootstrap";
import { useSelector } from "react-redux";

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

  return(
    <div>
      <Table>
        <thead>
          <tr>
            <th>#</th>
            <th>상품명</th>
            <th>수량</th>
            <th>변경하기</th>
          </tr>
        </thead>

        {/* Redux로 장바구니 상품 가져오기 */}
        {
          state.cartProduct.map((a,i)=>{
            return(
              <tbody>
                <tr>
                  <td>{(i+1)}</td>
                  <td>{state.cartProduct[i].name}</td>
                  <td>{state.cartProduct[i].count}</td>
                  <td>안녕</td>
                </tr>
              </tbody>
            )
          })
        }

      </Table>
    </div>
  )
}

export default Cart