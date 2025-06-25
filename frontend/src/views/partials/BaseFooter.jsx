import React from "react";

function BaseFooter() {
    return (
        <footer className="pt-lg-8 pt-5 footer bg-dark text-white" style={{ marginTop: "60px" }}>
            <div className="container mt-lg-2">
                <div className="row">
                    <div className="col-lg-4 col-md-6 col-12 text-white">
                        {/* about company */}
                        <div className="mb-4">
                            <h1>Certiﬁcation CDA</h1>
                            <div className="mt-4">
                                <p>Certiﬁcation CDA is feature-rich components and beautifully Bootstrap UIKit for developers, built with bootstrap responsive framework.</p>
                                {/* social media */}
                               
                            </div>
                        </div>
                    </div>
                   
                   
                    
                </div>
                <div className="row align-items-center g-0 border-top py-2 mt-6">
                    {/* Desc */}
                    <div className="col-md-10 col-12">
                        <div className="d-lg-flex align-items-center">
                            <div className="me-4">
                                <span>
                                    ©<span id="copyright5"></span>
                                    Certiﬁcation CDA
                                </span>
                            </div>
                            <div>
                                <nav className="nav nav-footer">
                                    <a className="nav-link text-white ps-0" href="#">
                                        Privacy Policy
                                    </a>
                                    <a className="nav-link text-white px-2 px-md-3" href="#">
                                        Cookie Notice
                                    </a>
                                    <a className="nav-link text-white d-none d-lg-block" href="#">
                                        Do Not Sell My Personal Information
                                    </a>
                                    <a className="nav-link text-white" href="#">
                                        Terms of Use
                                    </a>
                                </nav>
                            </div>
                        </div>
                    </div>
                    {/* Links */}
                    <div className="col-12 col-md-2 d-md-flex justify-content-end">
                        <div className="dropdown">
                            <a href="#" className="dropdown-toggle text-body" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                                <i className="fe fe-globe me-2 align-middle" />
                                Language
                            </a>
                            <ul className="dropdown-menu" aria-labelledby="dropdownMenuLink">
                                <li>
                                    <a className="dropdown-item" href="#">
                                        
                                        English
                                    </a>
                                </li>
                                <li>
                                    <a className="dropdown-item" href="#">
                                        
                                        Français
                                    </a>
                                </li>
                              
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    );
}

export default BaseFooter;
