/* eslint-disable */
import { createContext, useState } from 'react';
import { Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import './App.css';
import bg from './img/bg.png';
import data from './data.js';
import { Routes, Route, Link, useNavigate, Outlet } from 'react-router-dom'
import DetailCard from './routes/Detail.js';
import axios from 'axios';



function App() {

  let [shoes, setShoes] = useState(data); //data.js의 데이터 import
  let navigate = useNavigate();
  const cnt = 0;

 
  return (
    <div className="App">
      {/* navbar */}
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
              <Row md={3}>
                { shoes.map((data,i)=>{
                    return <Card shoes={shoes[i]} key={i} i={i}></Card>
                })}
              </Row>
            </Container>
            
            {/* 버튼을 눌러 ajax로 데이터 가져오기 */}
            <button onClick={()=>{
              //ajax로 데이터 가져오기 (axios 사용)
              axios.get('https://codingapple1.github.io/shop/data2.json')
              .then((result)=>{ //ajax 데이터 가져오기 성공한 경우
                let copy = [...shoes, ...result.data];
                setShoes(copy);
              })

              /* ajax로 데이터 서버로 보내기 */
              //axios.post('/url', {data   ex) {name : 'noi'}})

              /* n개의 url에서 데이터 가져오기 */
              //Promise.all([ axios.get('/url1'), axios.get('/url2') ])
              //.then(()=>{  실행할코드  })

              .catch((error)=>{
                console.log(error.response)
              });
            }} >more</button>
          </>
        }></Route>
        
        {/* 상세페이지 */}
        <Route path="/detail/:id" element={ <DetailCard shoes={shoes} /> }/>

        {/* 예외처리페이지 */}
        <Route path="*" element={<div>없는 페이지예요</div>} ></Route>  {/*만들어놓은 route 외의 모든 주소 */}
      </Routes>
    </div>
  );
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





              