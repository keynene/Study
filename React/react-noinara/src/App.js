/* eslint-disable */ //warning 제거
import { useState } from 'react';
import { Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import './App.css';
import data from './data.js';
import { Routes, Route, Link, useNavigate, Outlet } from 'react-router-dom';
import Detail from './routes/detail.js';
import axios from 'axios';


function App() {

  let [shoes,setShoes] = useState(data)
  let navigate = useNavigate()
  
  
  return (
    <div className="App">

      {/* Navbar */}
      <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand href="/" >NOI ·_· NARA</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link onClick={()=>{ navigate('/') }} >Home</Nav.Link>
            <Nav.Link onClick={()=>{ navigate('/detail/0') }} >Detail</Nav.Link>
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
            <Container>
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

            {/* Ajax 버튼누르면 데이터 더 받아오기 */}
            <button onClick={()=>{
              axios.get('https://codingapple1.github.io/shop/data2.json')
              .then((result)=>{
                
                // let copy = [...shoes]
                // let newdata = copy.concat(result.data)
                // setShoes(newdata)
                
                let copy = [...shoes, ...result.data]
                setShoes(copy)
              })
              .catch(()=>{
                console.log('실패함 ㅅㄱ')
              })
            }} >버튼</button>

          </div>
        } ></Route>
        {/* 상세페이지 / url파라미터 이용 */}
        <Route path='/detail/:id' element={<Detail shoes={shoes} />} ></Route>

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
  return (
    <Col sm>
      <img src={"https://codingapple1.github.io/shop/shoes"+ (props.i+1) +".jpg"} width="80%"/>
      <h4>{props.shoes[props.i].title}</h4>
      <p>{props.shoes[props.i].price}</p>
    </Col>
  )
}

export default App;
