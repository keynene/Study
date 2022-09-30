/* eslint-disable */
import { useState } from 'react';
import { Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import './App.css';
import bg from './img/bg.png';
import data from './data.js';


function App() {

  let [shoes] = useState(data); //data.js의 데이터 import
 
  return (
    <div className="App">
      <Navbar className="nav">  
        <Container>
          <Navbar.Brand href="#home">NOI ·_· NARA</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#best">Best</Nav.Link>
            <Nav.Link href="#new">New</Nav.Link>
            <Nav.Link href="#cart">Cart</Nav.Link>
            <Nav.Link href="#sale">Sale</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <div className="main-bg" style={{backgroundImage : 'url('+bg+')'}}></div>
      <Container>
        <Row>
          {
            shoes.map(function(data,i){
              return (
              <Card shoes={shoes[i]} key={i} i={i}></Card>
            )})
          }
        </Row>
      </Container>
    </div>
  );
}

function Card(props){
  return(
    <Col>
      <img src={'https://codingapple1.github.io/shop/shoes'+(props.i+1)+'.jpg'} width="80%"/>
      <h4>{props.shoes.title}</h4>
      <p>{props.shoes.content}</p>
      <p>{props.shoes.price}</p>
    </Col>
  )
}


export default App;