/* eslint-disable */ //warning 제거
import { lazy, Suspense, useEffect, useState } from 'react';
import { Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import { Routes, Route, Link, useNavigate, Outlet, useParams } from 'react-router-dom';
import './App.css';

/* Ajax용 파일 */
import axios from 'axios';
import { useQuery } from '@tanstack/react-query';

/* 기존 데이터 파일 */
import data from './data.js';

/* 컴포넌트 js파일 */
// import Detail from './routes/Detail.js';
// import Cart from './routes/Cart.js';

/* lazy : App.js 실행 시 보이지 않는 컴포넌트 js파일을 늦게 import하게 하는 함수
        : 해당 컴포넌트가 필요할 때만 import 
        : 별도의 js파일로 분리될 것 */
const Detail = lazy(() => import('./routes/Detail.js'));
const Cart = lazy(() => import("./routes/Cart.js"));
const Memo = lazy(() => import("./routes/Memo.js"));



function App() {

  let [shoes, setShoes] = useState(data) //신발데이터
  let [show, setShow] = useState(false) //데이터로딩화면 출력유무
  let [more, setMore] = useState(true) //데이터없을떄화면 출력유무
  let [pushcnt, setPushcnt] = useState(2) //더보기버튼 누른횟수
  let [stock, setStock] = useState([10,11,12]) //상품재고

  let navigate = useNavigate()
  
  /* Nav바 우측에 user이름 가져오기 */
  let result = useQuery(['작명'], ()=>{
    return axios.get('https://codingapple1.github.io/userdata.json')
    .then((axios_data)=>{ return axios_data.data })
    staleTime : 2000 //refetch(실시간 데이터 받아오기)시간 자율 조정 가능(2초로 설정함)
  })

  /* 최근 본 상품 */
  //Detail페이지 접속하면 상품id를 가져와서 localStorage에 추가 (Detail.js에 구현)
  useEffect(()=>{
    //이미 watched라는 localStorage에 값이 있으면 setItem하지말 것 (없을 때만 동작)
    localStorage.setItem('watched', JSON.stringify([]))
    if (localStorage.getItem('watched').length == 0){
      localStorage.setItem('watched', JSON.stringify([]))
    }
  },[])
  
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
            <Nav.Link onClick={()=>{ navigate('/memo') }} >Memo</Nav.Link>
            <Nav.Link onClick={()=>{ navigate('/about') }} >About</Nav.Link>
            <Nav.Link onClick={()=>{ navigate('/event') }} >Event</Nav.Link>
          </Nav>
          <Nav className="ms-auto">
            {/* { result.isLoading ? '로딩중' : '반가워요, ' + result.data.name } */}

            {/* 실제 데이터 있을 땐, 좀 더 가시적으로 아래와 같이 표현함 */}
            { result.isLoading && '로딩중' }
            { result.error && '에러남' }
            { result.data && '반가워요, ' + result.data.name }
          </Nav>

        </Container>
      </Navbar>

      {/* Router를 이용해 페이지 분리 */}
      {/* suspense : lazy로 js분리해놓은 파일 열 때 사용 */}
      {/* fallback : lazy로 js분리해놓은 파일 로딩중일 때 띄울 페이지 구현 가능 */}
      {/* 보통 Routes들 다 lazy로 분리해놓기 때문에 Suspense를 통째로 감싸는 경우가 많음 */}
      <Suspense fallback={ <div className="alert alert-warning">⏳...로딩중입니다...</div> }>
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
                  console.log(pushcnt)
                  //왜 state는 한박자 느리지?(한 번 기본값으로 동작 후 2번째 클릭부터 더함)

                  if (pushcnt <= 3){
                    axios.get('https://codingapple1.github.io/shop/data'+ pushcnt +'.json')
                    .then((result)=>{
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
          <Route path='/detail/:id' element={ <Detail shoes={shoes} /> } />

          {/* 장바구니페이지 */}
          <Route path="/cart" element={ <Cart shoes={shoes} /> } />

          {/* memo, useMemo페이지 */}
          <Route path="/memo" element={ <Memo /> } />

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
      </Suspense>
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
