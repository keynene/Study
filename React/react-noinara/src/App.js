/* eslint-disable */ //warning 제거
import { createContext, useEffect, useState } from 'react';
import { Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import { Routes, Route, Link, useNavigate, Outlet } from 'react-router-dom';
import './App.css';
import data from './data.js';
import Detail from './routes/Detail.js';
import Cart from './routes/Cart.js';
import axios from 'axios';

// context = state보관함
export let Context1 = createContext()


function App() {

  let [shoes, setShoes] = useState(data) //신발데이터
  let [show, setShow] = useState(false) //데이터로딩화면 출력유무
  let [more, setMore] = useState(true) //데이터없을떄화면 출력유무
  let [pushcnt, setPushcnt] = useState(2) //더보기버튼 누른횟수
  let [stock, setStock] = useState([10,11,12]) //상품재고

  let navigate = useNavigate()

  useEffect(()=>{
    // 더보기 버튼 눌렀는데 데이터 없을 때 에러메세지 출력 (출력하면 더보기 버튼 사라짐)
    {
      more == false
      ? alert("🙅🏻‍♀️더 이상 데이터가 없습니다!")
      : null
    }
  }, [pushcnt])

  
  
  return (
    <div className="App">

      {/* Navbar */}
      <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand href="/" >NOI ·_· NARA</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link onClick={()=>{ navigate('/') }} >Home</Nav.Link>
            <Nav.Link onClick={()=>{ navigate('/detail/0') }} >Detail</Nav.Link>
            <Nav.Link onClick={()=>{ navigate('/cart') }} >Cart</Nav.Link>
            <Nav.Link onClick={()=>{ navigate('/about') }} >About</Nav.Link>
            <Nav.Link onClick={()=>{ navigate('/event') }} >Event</Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      {/* Router를 이용해 페이지 분리 */}
      <Routes>
        {/* 메인페이지 */}
        <Route path="/" element={
          <div>
            {/* MainImg */}
            <div className="main-bg"></div> 

            {/* Product */}
            <Container className="product_container" >
              <Row md={3}>
                {/* shoes 자료들을 map을 이용해 갯수만큼 순차적으로 출력  */}
                {
                  shoes.map((a,i)=>{
                    return(
                      <Card shoes={shoes} i={i} key={i} />
                    )
                  })
                }
                
                {/* 아래와 같이 동작 */}
                {/* <Col sm>
                  <img src="https://codingapple1.github.io/shop/shoes1.jpg" width="80%"/>
                  <h4>{shose[0].title}</h4>
                  <p>{shose[0].price}</p>
                </Col>
                <Col sm>
                  <img src="https://codingapple1.github.io/shop/shoes2.jpg" width="80%"/>
                  <h4>{shose[1].title}</h4>
                  <p>{shose[1].price}</p>
                </Col>
                <Col sm>
                  <img src="https://codingapple1.github.io/shop/shoes3.jpg" width="80%"/>
                  <h4>{shose[2].title}</h4>
                  <p>{shose[2].price}</p>
                </Col> */}
                
              </Row>
            </Container>
            
            {/* 로딩화면UI */}
            {
              show == true
              ? <div className="alert alert-warning">⏳...로딩중입니다... </div>
              : null
            }


            {/* 버튼 누르면 데이터 더 받아오기(Ajax) / 데이터 없을 때 버튼 사라짐*/}
            {
              more == true
              ? // 데이터 있을 때
              <button onClick={()=>{
                setShow(true); //로딩화면 true
                setPushcnt(pushcnt+1); 
                //왜 state는 한박자 느리지?(한 번 기본값으로 동작 후 2번째 클릭부터 더함)
                
                // post방법
                // axios.post('/url',{name : 'kim'})

                // 여러 개 한 번에 get
                // Promise.all([ axios.get('/url1), axios.get('/url2) ])
                // .then(()=>{  }).catch(()=>{  })

                if (pushcnt <= 3){
                  axios.get('https://codingapple1.github.io/shop/data'+ pushcnt +'.json')
                  .then((result)=>{
                    
                    //concat : 배열 2개 합쳐서 새로운 배열에 넣기
                    // let copy = [...shoes]
                    // let newdata = copy.concat(result.data)
                    // setShoes(newdata)
                    
                    let copy = [...shoes, ...result.data]
                    setShoes(copy)
                    setShow(false); //로딩화면 false
                  })
                  .catch(()=>{
                    console.log('실패함 ㅅㄱ')
                    setShow(false); //로딩화면 false
                  })
                }

                else {
                  setShow(false); //로딩화면 false
                  setMore(false); //데이터출려유무 false
                }
              }} >더보기</button>

              :  //데이터 없을 때
              <div className="alert alert-warning"><p>🙅🏻‍♀️...끝 끝 쇼핑그만!...</p></div>
            }

          </div>
        } ></Route>
        {/* 상세페이지 / url파라미터 이용 */}
        <Route path='/detail/:id' element={
          /* 1. Context API */
          // Detail 컴포넌트로 공유하고 싶은 state Context1에 입력
          // <Context1.Provider value={{ stock, shoes }}> 
          //   <Detail shoes={shoes} />
          // </Context1.Provider>

          <Detail shoes={shoes} />
        } ></Route>

        {/* 장바구니페이지 */}
        <Route path="/cart" element={<Cart />} />

        {/* 어바웃페이지 / nested routes 이용 */}
        <Route path='/about' element={<About/>} >
          <Route path='member' element={<div>멤버페이지</div>} /> {/* /about/member */}
          <Route path='location' element={<div>위치정보</div>} /> {/* /about/location */}
        </Route>

        {/* 이벤트페이지 */}
        <Route path='/event' element={<Event/>} >
          <Route path="one" element={<p>첫 주문시 양배추즙 서비스</p>} />
          <Route path="two" element={<p>생일기념 쿠폰받기</p>} />
        </Route>

        {/* 예외처리 */}
        <Route path='*' element={<div>없는페이지예요</div>} />
      </Routes>
    </div>
  );
}

function Event(){
  return(
    <div>
      <h4>오늘의 이벤트</h4>
      <Outlet />
    </div>
  )
}

function About(){
  return(
    <div>
      <h4>회사정보임</h4>
      <Outlet />
    </div>
  )
}

function Card(props){
  let navigate = useNavigate()
  return (
    <Col sm >
      <div onClick={()=>{ navigate('/detail/'+props.i) }} >
        <img src={"https://codingapple1.github.io/shop/shoes"+ (props.i+1) +".jpg"} width="80%" />
        <h4>{props.shoes[props.i].title}</h4>
        <p>{props.shoes[props.i].price}</p>
      </div>
    </Col>
  )
}

export default App;
