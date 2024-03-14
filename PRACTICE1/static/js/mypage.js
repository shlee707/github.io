document.addEventListener('DOMContentLoaded', function() {
    const themeSelect = document.getElementById('theme');
  
    // 페이지가 로드될 때 저장된 테마를 불러와 적용
    applyTheme(getSavedTheme());
  
    // 테마 변경 시 이벤트 처리
    themeSelect.addEventListener('change', function() {
      const selectedTheme = themeSelect.value;
      applyTheme(selectedTheme);
      saveTheme(selectedTheme);
    });
  
    // 저장된 테마를 불러오는 함수
    function getSavedTheme() {
      return localStorage.getItem('theme') || 'light'; // 기본값은 'light'
    }
  
    // 테마를 적용하는 함수
    function applyTheme(theme) {
      document.body.className = ''; // 모든 클래스 제거
      document.body.classList.add(`theme-${theme}`); // 선택한 테마 클래스 추가
    }
  
    // 테마를 저장하는 함수
    function saveTheme(theme) {
      localStorage.setItem('theme', theme);
    }
  });
  