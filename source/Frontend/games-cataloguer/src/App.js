import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useLocation, Navigate } from 'react-router-dom';
import Header from './components/Header';
import GameGrid from './components/GameGrid';
import Login from './components/Login';
import SearchBar from './components/SearchBar';
import Wishlist from './components/Wishlist';
import CreateAccount from './components/CreateAccount';

function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  );
}

function AppContent() {
  const location = useLocation();
  const [searchQuery, setSearchQuery] = useState('');

  return (
    <>
      {location.pathname !== '/create-account' && location.pathname !== '/login' && <Header />}
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <SearchBar setSearchQuery={setSearchQuery} />
              <GameGrid searchQuery={searchQuery} />
            </ProtectedRoute>
          }
          />
        <Route
          path="/wishlist"
          element={
            <ProtectedRoute>
              <Wishlist />
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/create-account" element={<CreateAccount />} />
      </Routes>
    </>
  );
}

function ProtectedRoute({ children }) {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  return isLoggedIn ? children : <Navigate to="/login" />;
}

export default App;