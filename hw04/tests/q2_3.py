test = {
  'name': 'q2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Double check that your salary_range function is correct;
          >>> salary_range(make_array(5, 1, 20, 1000)) == 999
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure that the table has teams as the rows and positions as the columns.;
          >>> set(["Team", "C", "PF", "PG", "SF", "SG"]) == set(team_position_ranges.labels)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(team_position_ranges.column(1))
          393301627
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
