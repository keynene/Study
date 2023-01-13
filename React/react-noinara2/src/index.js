import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter } from "react-router-dom"
import { Provider } from 'react-redux';
import store from './store.js'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import * as serviceWorkerRegistration from './serviceWorkerRegistration';


const queryClient = new QueryClient()

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <QueryClientProvider client={queryClient}>
      <Provider store={store}> 
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </Provider>
    </QueryClientProvider>
  // </React.StrictMode>
  );
  
  // <React.StrictMode> 
  // 예기치 못한 에러 처리하기 위한 컴포넌트인데, 렌더 2번 시키기 때문에 alert를 2번 호출하는 오류발생해서 주석처리해놨음
  //Provider = redux store 가져오기

  serviceWorkerRegistration.register();


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
