const TODAY = new Date().toISOString().split('T')[0];

function getDatesInMonth(dateStr) {
  const d = new Date(dateStr);

  const year = d.getFullYear();

  const month = d.getMonth();
  
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  
  const dates = [];
  
  for (let i = 1; i <= daysInMonth; i++) {
    const dateObj = new Date(year, month, i);
    const dateString = dateObj.toISOString().split('T')[0];
    dates.push(dateString);
  }
  
  return dates;
}

function getDatesInYear() {
  const year = new Date().getFullYear(); 
  const dates = []; 
  
  for (let month = 0; month < 12; month++) {
    const days = new Date(year, month + 1, 0).getDate();
	
    for (let day = 1; day <= days; day++) {
      const dateString = new Date(year, month, day).toISOString().split('T')[0];
      dates.push(dateString);
    }
  }
  
  return dates;
}

function calculateStreaks(records, allDates) {
  
  let current = 0;
  let best = 0;
  let temp = 0;
  
  allDates.forEach(date => {
    if (records[date] === true) {
      temp++;
      current = temp;
      if (temp > best) best = temp;
    } else {
      temp = 0;
    }
  });

  const todayIndex = allDates.indexOf(TODAY);
  
  if (todayIndex === -1) return { current: 0, best };
  
  current = 0;
  for (let i = todayIndex; i >= 0; i--) {
    if (records[allDates[i]] === true) {
      current++;
    } else {
      break;
    }
  }

  return { current, best };
}

function getCompletedCount(records, allDates) {
  const completed = allDates.filter(d => records[d]).length;
  return { completed, total: allDates.length };
}

function isGoalMet(habit, records, weekDates) {
  const completedInWeek = weekDates.filter(d => records[d]).length;
  
  if (habit.goal === 'daily') {
    return completedInWeek === 7;
  }
  if (habit.goal === '3x') {
    return completedInWeek >= 3;
  }
  if (habit.goal === 'weekends') {
    const weekendDates = weekDates.filter(d => {
      const dayOfWeek = new Date(d).getDay();
      return dayOfWeek === 0 || dayOfWeek === 6;
    });
    const completedWeekends = weekendDates.filter(d => records[d]).length;
    return completedWeekends === weekendDates.length;
  }

  return false;
}

function getGroupColor(group) {
  const colors = {
    'Здоровье': '#2ecc71',    
    'Образование': '#3498db',
    'Работа': '#e74c3c', 
    'Другое': '#9b59b6'
  };
  return colors[group] || '#7f8c8d';
}

function loadData() {
  const data = localStorage.getItem('habitTrackerFull');
  
  if (!data) return { habits: [], records: {} };

  return JSON.parse(data);
}

function saveData(data) {
  const jsonString = JSON.stringify(data);
  localStorage.setItem('habitTrackerFull', jsonString);
}

function renderHabits() {
  const data = loadData();

  const allDates = getDatesInMonth(TODAY);

  const weekStart = new Date(TODAY);

  const dayOfWeek = weekStart.getDay();
  let diff = weekStart.getDate() - dayOfWeek + (dayOfWeek === 0 ? -6 : 1);
  weekStart.setDate(diff);

  const weekDates = [];
  for (let i = 0; i < 7; i++) {
    const d = new Date(weekStart);
    d.setDate(weekStart.getDate() + i);
    weekDates.push(d.toISOString().split('T')[0]);
  }

  const activeHabits = data.habits.filter(h => !h.archived);
  const activeContainer = document.getElementById('habitsContainer');
  activeContainer.innerHTML = '';
  
  if (activeHabits.length === 0) {
    activeContainer.innerHTML = '<p>Нет активных привычек.</p>';
  } else {
    activeHabits.forEach(habit => {
      renderHabitCard(habit, data.records, allDates, weekDates, activeContainer, false);
    });
  }

  const archivedHabits = data.habits.filter(h => h.archived);
  const archiveContainer = document.getElementById('archiveContainer');
  const archiveSection = document.getElementById('archiveSection');
  archiveContainer.innerHTML = '';
  
  if (archivedHabits.length > 0) {
    archiveSection.style.display = 'block'; 
    archivedHabits.forEach(habit => {
      renderHabitCard(habit, data.records, allDates, weekDates, archiveContainer, true);
    });
  } else {
    archiveSection.style.display = 'none';
  }

  renderYearCalendar();
}

function renderHabitCard(habit, recordsObj, allDates, weekDates, container, isArchived = false) {
  const records = recordsObj[habit.id] || {};
  
  const { current, best } = calculateStreaks(records, allDates);
  const { completed, total } = getCompletedCount(records, allDates);
  const goalMet = isGoalMet(habit, records, weekDates);

  const card = document.createElement('div');
  card.className = `habit-card ${isArchived ? 'archived' : ''}`;

  card.innerHTML = `
    <div class="habit-header">
      <div>>
        <div class="habit-name">${habit.name}</div>
        <span class="habit-group-tag" style="background:${getGroupColor(habit.group)}">
          ${habit.group}
        </span>
      </div>
      <div class="actions">
        ${!isArchived ? `
          <button class="btn btn-edit" data-id="${habit.id}">✏️</button>
          <button class="btn btn-archive" data-id="${habit.id}">📦 Архив</button>
          <button class="btn btn-reset" data-id="${habit.id}">🔄</button>
          <button class="btn btn-delete" data-id="${habit.id}">🗑️</button>
        ` : `
          <button class="btn btn-restore" data-id="${habit.id}">↩️ Вернуть</button>
          <button class="btn btn-delete" data-id="${habit.id}">🗑️ Удалить</button>
        `}
      </div>
    </div>
    ${!isArchived ? `
      <div class="habit-stats">
        <span>Серия: <span class="streak">${current}</span> (лучшая: ${best})</span>
        <span>Выполнено: ${completed}/${total} (${Math.round((completed / total) * 100 || 0)}%)</span>
        <span>Цель на неделю: ${goalMet ? '✅' : '❌'}</span>
      </div>
      <div class="week-grid">
        ${weekDates.map(date => {
          const shortName = new Date(date).toLocaleDateString('ru', { weekday: 'short' }).slice(0,1).toUpperCase();
          const isDone = records[date] || false;
          return `<div class="day-box ${isDone ? 'done' : ''}" 
                     data-date="${date}" 
                     data-id="${habit.id}">
                    ${isDone ? '✓' : shortName}
                  </div>`;
        }).join('')}
      </div>
    ` : ''}
  `;

  container.appendChild(card);
}

function renderYearCalendar() {
  const grid = document.getElementById('calendarGrid');
  const data = loadData();
  const yearDates = getDatesInYear();

  grid.innerHTML = '';

  yearDates.forEach(date => {
    const dayEl = document.createElement('div');
    dayEl.className = 'year-day'; 
    
    let anyDone = false;
    data.habits.forEach(habit => {
      if (habit.archived) return;
      if (data.records[habit.id]?.[date]) {
        anyDone = true;
      }
    });
    
    if (anyDone) {
      dayEl.classList.add('done');
    }
    
    grid.appendChild(dayEl);
  });
}

document.getElementById('addHabitForm').addEventListener('submit', e => {
  e.preventDefault();

  const nameInput = document.getElementById('habitName');
  const groupSelect = document.getElementById('habitGroup');
  const goalSelect = document.getElementById('habitGoal');
  const errorEl = document.getElementById('formError');

  const name = nameInput.value.trim();
  const group = groupSelect.value;
  const goal = goalSelect.value;

  errorEl.textContent = ''; 

  if (!name) {
    errorEl.textContent = 'Введите название';
    return; 
  }

  const data = loadData();

  const newHabit = {
    id: Date.now(),       
    name: name,
    group: group,
    goal: goal,
    archived: false       
  };

  data.habits.push(newHabit);

  if (!data.records[newHabit.id]) {
    data.records[newHabit.id] = {};
  }

  saveData(data);

  renderHabits();

  nameInput.value = '';
});

document.getElementById('toggleArchive').addEventListener('click', () => {
  const archiveSection = document.getElementById('archiveSection');
  const isVisible = archiveSection.style.display === 'block';
  archiveSection.style.display = isVisible ? 'none' : 'block';
  const button = document.getElementById('toggleArchive');
  button.textContent = isVisible ? 'Показать архив' : 'Скрыть архив';
});

document.addEventListener('click', e => {
  const data = loadData();

  if (e.target.classList.contains('day-box')) {
    const habitId = Number(e.target.dataset.id);
    const habit = data.habits.find(h => h.id === habitId);

    if (habit?.archived) return;

    const date = e.target.dataset.date; 
    const records = data.records[habitId] || {};

    records[date] = !records[date];
    data.records[habitId] = records;

    saveData(data);
    renderHabits();
    return;
  }

  const btn = e.target.closest('.btn'); 
  if (!btn) return;

  const habitId = Number(btn.dataset.id);
  const habitIndex = data.habits.findIndex(h => h.id === habitId);
  if (habitIndex === -1) return;

  if (btn.classList.contains('btn-delete')) {
    data.habits.splice(habitIndex, 1);
    delete data.records[habitId];
  } else if (btn.classList.contains('btn-reset')) {
    data.records[habitId] = {};
  } else if (btn.classList.contains('btn-archive')) {
    data.habits[habitIndex].archived = true;
  } else if (btn.classList.contains('btn-restore')) {
    data.habits[habitIndex].archived = false;
  } else if (btn.classList.contains('btn-edit')) {
    const newName = prompt('Измените название:', data.habits[habitIndex].name);
    if (newName && newName.trim()) {
      data.habits[habitIndex].name = newName.trim();
    }
  }

  saveData(data);
  renderHabits();
});

document.addEventListener('DOMContentLoaded', () => {
  if (!localStorage.getItem('habitTrackerFull')) {
    localStorage.setItem('habitTrackerFull', JSON.stringify({ habits: [], records: {} }));
  }
  renderHabits();
});