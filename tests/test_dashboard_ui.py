import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from pandas import Timestamp
from src.dashboard_ui import DashboardUI


def test_load_css_reads_file_and_sets_markdown():
    with patch("builtins.open", new_callable=MagicMock) as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = "mock_css"
        with patch("streamlit.markdown") as mock_markdown:
            DashboardUI().load_css()
            mock_markdown.assert_called_once_with('<style>mock_css</style>', unsafe_allow_html=True)


def test_display_title_sets_markdown():
    with patch("streamlit.markdown") as mock_markdown:
        with patch.object(DashboardUI, "load_css"):
            DashboardUI().display_title("Test Title")
            mock_markdown.assert_called_once_with("Test Title", unsafe_allow_html=True)


def test_display_columns_inputs_returns_correct_values():
    with patch("streamlit.columns") as mock_columns:
        mock_columns.return_value = [MagicMock(), MagicMock(), MagicMock(), MagicMock()]
        result = DashboardUI().display_columns_inputs()
        assert len(result) == 4


def test_setup_layout_returns_correct_columns():
    with patch("streamlit.columns") as mock_columns:
        mock_columns.return_value = [MagicMock(), MagicMock()]
        result = DashboardUI().setup_layout()
        assert len(result) == 2


def test_setup_tabs_returns_correct_tabs():
    with patch("streamlit.tabs") as mock_tabs:
        mock_tabs.return_value = [MagicMock(), MagicMock()]
        result = DashboardUI().setup_tabs()
        assert len(result) == 2


def test_display_time_info_sets_correct_markdown():
    with patch("streamlit.columns") as mock_columns:
        mock_columns.return_value = [MagicMock(), MagicMock()]
        with patch("streamlit.markdown") as mock_markdown:
            DashboardUI().display_time_info(Timestamp("2022-01-01"), 60)
            assert mock_markdown.call_count == 2


def test_display_summary_boxes_sets_correct_metrics():
    with patch("streamlit.container"):
        with patch("streamlit.columns") as mock_columns:
            mock_columns.return_value = [MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock()]
            with patch("streamlit.metric") as mock_metric:
                DashboardUI().display_summary_boxes(pd.DataFrame({
                    'Monthly Repayment': [500, 500],
                    'Principal Paid': [200, 200],
                    'Interest Paid': [100, 100],
                    'Admin Fee': [50, 50],
                    'Total Payment': [850, 850]
                }))
                assert mock_metric.call_count == 5
