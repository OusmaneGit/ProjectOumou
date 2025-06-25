import React, { useEffect } from "react";
import { Link, useParams } from "react-router-dom";

import BaseHeader from "../partials/BaseHeader";
import BaseFooter from "../partials/BaseFooter";



function Success() {
    
    
    const param = useParams();
    const urlParam = new URLSearchParams(window.location.search);
    const sessionId = urlParam.get("session_id");
  

    console.log(sessionId);
   
    console.log(param);

    useEffect(() => {
        const formdata = new FormData();

       
        formdata.append("session_id", sessionId);
       

        
    }, []);

  

    return (
        <>
            <BaseHeader />

            <section className="pt-0  position-relative overflow-hidden my-auto">
                <div className="container position-relative">
                    <div className="row g-5 align-items-center justify-content-center">
                        
                        {(
                            <>
                                <div className="col-lg-5">
                                    <h1 className="text-success">Enrollment Successful!</h1>
                                    <p>Your enrollment was successfull, please visit your dashboard to start course now.</p>
                                </div>
                                <div className="col-lg-7 text-center">
                                    <img src="https://i.pinimg.com/originals/0d/e4/1a/0de41a3c5953fba1755ebd416ec109dd.gif" className="h-300px h-sm-400px h-md-500px h-xl-700px" alt="" />
                                </div>
                            </>
                        )}

                       
                       

                        

                        
                    </div>
                </div>
            </section>

            <BaseFooter />
        </>
    );
}

export default Success;
