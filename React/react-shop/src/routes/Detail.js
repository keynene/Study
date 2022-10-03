/* eslint-disable */
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import styled from 'styled-components'

// let YellowBtn = styled.button`
//   background : ${ props => props.bg }; //yellow 로 하고싶은 경우 react html코드에서 bg="yellow"
//   color : ${ props => props.bg == 'blue' ? 'white' : 'black' }; //bg가 blue인경우 white, blue가 아니면 black
//   padding : 10px;
// `

//  let NewBtn = styled.button(YellowBtn)` //상속가능 (YellowBtn상속한 상태)
//   font-weight : bold;
//  `

// class Detail2 extends React.Component {
//   componentDidMount(){
//     //컴포넌트가 mount시 여기 코드 실행
//   }
//   componentDidUpdate(){
//     //컴포넌트가 update시 여기 코드 실행
//   }
//   componentWillUnmount(){
//     //컴포넌트가 unmount시 여기 코드 실행
//   }
// }

function DetailCard(props){

  let {id} = useParams(); //app.js에서 detail/:id 로 정의했는데 여기 들어가는 id를 저장함
  let found = props.shoes.find(function(x){
    return x.id == id;
  })
  let [time, setTime] = useState(true);
  let [num, setNum] = useState('');
  

  useEffect(()=>{
    //mount, update시 코드 실행
    let timer = setTimeout(()=>{ setTime(false) },2000); //보통 타이머는 변수에 저장해서 사용 (삭제 or 재사용 가능하게)
    if (isNaN(num) == true){
      alert("숫자만 입력하라니까!");
    }

    return ()=>{
      //useEffect동작 전에 실행   (ex. clean up function)
      //ex. react 특성상 위의 setTimeout 코드가 계속 실행되어 타이머가 몇천개 되므로 삭제해줄 필요가 있음 (unmount)
      clearTimeout(timer);
    }
  }, [num]) 
  //뒤에 ", []"추가해주면 최초 mount될 때 1회만 실행됨 (update될 떄는 실행 x)
  //뒤에 ", [alert]"추가해주면 alert가 변화될 때마다 실행됨

  return (
    <div className="container">
      {
        time == true ?
        <div className="alert alert-warning">
          2초이내 구매시 할인
        </div>
        : null
      }
      
      <div className="row">
        <div className="col-md-6">
          <img src={"https://codingapple1.github.io/shop/shoes"+(parseInt(found.id)+1)+".jpg"} width="100%" />
        </div>
        <div className="col-md-6">
          <input placeholder="숫자만 입력해주세요!" onChange={(e)=>{ 
            setNum(e.target.value)
          }} />
          <h4 className="pt-5">{found.title}</h4>
          <p>{found.content}</p>
          <p>{found.price}</p>
          <button className="btn btn-danger">주문하기</button> 
        </div>
      </div>
    </div> 
  )
}


export default DetailCard;