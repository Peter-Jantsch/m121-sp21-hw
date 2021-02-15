test = {
  'name': 'q2_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure that the table has a column called Team and a column called count.;
          >>> set(["Team", "count"]) == set(teams_and_counts.labels)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you do not include teams that don't have positions with average salary above 15m.;
          >>> teams_and_counts.num_rows
          18
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
