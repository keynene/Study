/* eslint-disable */ //warning 제거
import { useState } from 'react';
import { Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import './App.css';
import data from './data.js';
import { Routes, Route, Link } from 'react-router-dom';
import DetailCard from './detail.js';


function App() {
  let [shoes,setShoes] = useState(data)
  
  
  return (
    <div className="App">

      {/* Navbar */}
      <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand href="/">NOI ·_· NARA</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/detail">Detail</Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      {/* Router를 이용해 페이지 분리 */}
      <Routes>
        {/* 메인페이지 */}
        <Route path="/" element={
          <>
            {/* MainImg */}
            <div className="main-bg"></div> 

            {/* Product */}
            <Container>
              <Row>
                {/* shoes 자료들을 map을 이용해 갯수만큼 순차적으로 출력  */}
                {
                  shoes.map((a,i)=>{
                    return(
                      <Card shoes={shoes} i={i} />
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
          </>
        } ></Route>
        <Route path='/detail' element={<DetailCard shoes={shoes} />} ></Route>

      </Routes>
    </div>
  );
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
