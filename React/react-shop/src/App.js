/* eslint-disable */
import { useState } from 'react';
import { Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import './App.css';
import bg from './img/bg.png';
import data from './data.js';
import { Routes, Route, Link, useNavigate, Outlet } from 'react-router-dom'
import DetailCard from './routes/Detail.js';

function App() {

  let [shoes] = useState(data); //data.js의 데이터 import
  let navigate = useNavigate();
 
  return (
    <div className="App">


      <Navbar className="nav">  
        <Container>
          <Navbar.Brand href="/">NOI ·_· NARA</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link onClick={()=>{ navigate('/') }} href="#home" >Home</Nav.Link>
            <Nav.Link onClick={()=>{ navigate('/detail') }} href="#detail" >Detail</Nav.Link>
            <Nav.Link href="#new">New</Nav.Link>
            <Nav.Link href="#cart">Cart</Nav.Link>
            <Nav.Link href="#sale">Sale</Nav.Link>
          </Nav>
        </Container>
      </Navbar>


      <Routes>
        {/* 메인페이지 */}
        <Route path="/" element={ 
          <>
            <div className="main-bg" style={{backgroundImage : 'url('+bg+')'}}></div>
            <Container>
              <Row>
                { shoes.map((data,i)=>{
                    return <Card shoes={shoes[i]} key={i} i={i}></Card>
                })}
              </Row>
            </Container>
          </>
        }></Route>
        
        <Route path="/detail/:id" element={<DetailCard shoes={shoes}></DetailCard>} />

        {/* 
          Nested Route
          route안에 route를 넣는 작업
          nested route 접속 시 element 2개나 보임
        */}
        <Route path="/about" element={<About />} >
          {/*Outlet을 통해 about/member로 접속하면 about과 member를 동시에 보여줌*/}
          <Route path="member" element={<div>멤버임</div>}></Route> 
          <Route path="location" element={<div>위치정보임</div>} ></Route>
        </Route>
        <Route path="/event" element={<Event />} >
          <Route path="one" element={<div>첫 주문시 양배추즙 서비스</div>} ></Route>
          <Route path="two" element={<div>생일기념 쿠폰받기</div>} ></Route>
        </Route>

        <Route path="*" element={<div>없는 페이지예요</div>} ></Route>  {/*만들어놓은 route 외의 모든 주소 */}
      </Routes>


      
    </div>
  );
}

function Event(){
  return (
    <div>
      <h4>오늘의 이벤트</h4>
      <Outlet></Outlet>
    </div>
  )
}

function About(){
  return (
    <div>
      <h4>회사정보임</h4>
      <Outlet></Outlet>
    </div>
  )
}

function Card(props){
  return(
    <Col sm>
      <img src={'https://codingapple1.github.io/shop/shoes'+(props.i+1)+'.jpg'} width="80%"/>
      <h4>{props.shoes.title}</h4>
      <p>{props.shoes.content}</p>
      <p>{props.shoes.price}</p>
    </Col>
  )
}


export default App;